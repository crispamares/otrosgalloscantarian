import model
import math
from parlamento import *
from google.appengine.api import memcache

from escanosProv2004 import escanosProvincia2004
from escanosProv2008 import escanosProvincia2008


class LeyDHont:
    def __init__(self, ano, th=0.03):
        self.diputadosProvincias = {}
        self.threshold = th
        self.ano = ano
        self.censos = model.CensoElectoral.all()
        self.censos.filter("ano =",ano)
        self.key = "VotosProvinciales"+ano
        self.pucherazo = None
        self.caciques = []
        self.geolocalizacionEscanos = {}

    def geolocalizarEscanos(self,diputado,provincia,numEscanos):
        partido = diputado[1]

        # La primera vez que se registra un partido se inicia su key
        if partido not in self.geolocalizacionEscanos:
            self.geolocalizacionEscanos[partido] = []

        # Comprobamos si ya se ha votado anteriormente a ese partido en la
        # provincia
        for i in range(0,len(self.geolocalizacionEscanos[partido])):
            # En caso de ser asi, se incrementa y se devuelve la funcion
            if self.geolocalizacionEscanos[partido][i][0] == provincia:
                self.geolocalizacionEscanos[partido][i][1] += numEscanos
                return
        # En caso de ser la primera vez que se vota en la provincia
        # se incrementan los escanos
        self.geolocalizacionEscanos[partido] += [[provincia,numEscanos]]

    def manipular(self, caciques, pucherazo):
        self.caciques = caciques
        self.pucherazo = pucherazo

    def repartirEscanos(self):
        parlamento = Parlamento(350)

        diputadosProvinciales = {}

        # Asignar diputados fijos de las provincias
        poblacionDeDerecho = 0
        #print "Provincias"
        for censoProvincia in self.censos:
            provincia = censoProvincia.provincia
            #print provincia
            poblacionDeDerecho += censoProvincia.censoTotal
            candidaturas = self.candidaturasMayoritarias(censoProvincia)
            diputadosProvinciales[provincia] = self.asignarDiputados(candidaturas,provincia)
            #print "Diputados Provinciales"
            #print diputadosProvinciales[provincia]

            # Se elijen dos diputados de cada provincia a excepcion de ceuta y melilla
            diputado = diputadosProvinciales[provincia].pop()
            parlamento.anadirDiputados(diputado)
            self.geolocalizarEscanos(diputado,provincia,1)
            if (provincia != "Ceuta" and provincia != "Melilla"):
                diputado = diputadosProvinciales[provincia].pop()
                parlamento.anadirDiputados(diputado)
                self.geolocalizarEscanos(diputado,provincia,1)

        # Asignar diputados por poblacion
        cuotaReparto = 1.0 * poblacionDeDerecho / parlamento.asientosLibres
        #print "Cuota Reparto", cuotaReparto

        coeficientes = []
        for censoProvincia in self.censos:
            provincia = censoProvincia.provincia
            coeficiente = censoProvincia.censoTotal / cuotaReparto
            numDiputadosPorPoblacion = math.floor(coeficiente)
            coeficiente -= numDiputadosPorPoblacion
            coeficientes += [(coeficiente,provincia)]
            while (numDiputadosPorPoblacion > 0):
                diputado = diputadosProvinciales[provincia].pop()
                parlamento.anadirDiputados(diputado)
                self.geolocalizarEscanos(diputado,provincia,1)
                numDiputadosPorPoblacion -= 1

        # Asignar los diputados restantes segun coeficientes
        coeficientes.sort()
        while (parlamento.asientosLibres > 0):
            (coef,provincia) = coeficientes.pop()
            diputado = diputadosProvinciales[provincia].pop()
            parlamento.anadirDiputados(diputado)
            self.geolocalizarEscanos(diputado,provincia,1)

        #print self.geolocalizacionEscanos['CiU']
        parlamento.geolocalizar(self.geolocalizacionEscanos)

        return parlamento

    # Devuelve la lista de candidaturas que alcanzan el porcentaje
    # minimo establecido por la ley d'Hont
    def candidaturasMayoritarias(self, censoProvincia):
        keyProvincia = self.key+censoProvincia.provincia
        votos = memcache.get(keyProvincia)
        if votos is None:
            escrutinios = model.Escrutinio.all()
            escrutinios.filter("censo  =",censoProvincia)
            votos = {}
            for escrutinio in escrutinios:
                votos[escrutinio.partido] = escrutinio.votos
            memcache.add(keyProvincia,votos)
        # Filtrar candidaturas que no alcanzan el threshold de la ley
        totalVotos = censoProvincia.votosTotales

        if self.pucherazo is not None:
            #print "Dando pucherazo!"
            votosBlanco = censoProvincia.votosBlanco
            votos = self.pucherazo.darPucherazo(votos,votosBlanco,self.caciques)
        candidaturasValidas = {}
        #print "Votos en ", censoProvincia.provincia
        #print votos
        for partido in votos:
            if ((1.0*votos[partido]/totalVotos) > self.threshold):
                candidaturasValidas[partido] = votos[partido]
        return candidaturasValidas


    # Calcula los coeficientes de cada candidatura
    def asignarDiputados(self, candidaturas, provincia):
        numDiputados = 0
        if (eval(self.ano) <= 2004):
            numDiputados = escanosProvincia2004[provincia]
        else:
            numDiputados = escanosProvincia2008[provincia]
        #print "Asignando ", numDiputados, " escanos"
        diputados = []
        # Divide los votos entre el numero de diputados de la provincia
        for partido in candidaturas:
            votos = candidaturas[partido]
            for i in range(1,numDiputados+1):
                diputados += [(1.0*votos/i,partido)]

        # Reordena los votos obtenidos
        diputados.sort()
        #print "Diputados por provincia"
        #print diputados
        return diputados
