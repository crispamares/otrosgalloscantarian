import model
import math
from parlamento import *
from google.appengine.api import memcache

from escanosProv2004 import escanosProvincia2004
from escanosProv2008 import escanosProvincia2008


class LeyNacionalDHont:
    def __init__(self, ano, th=0.03):
        self.threshold = th
        self.ano = ano
        self.censos = model.CensoElectoral.all()
        self.censos.filter("ano =",ano)
        self.key = "LeyNacnionalDHont"+ano
        self.pucherazo = None
        self.caciques = []
        self.totalVotos = 0
        self.totalVotosBlanco = 0

    def manipular(self, caciques, pucherazo):
        self.caciques = caciques
        self.pucherazo = pucherazo

    def repartirEscanos(self):
        parlamento = Parlamento(350)

        votos = memcache.get(self.key+"VotosCandidaturas")
        self.totalVotos = memcache.get(self.key+"TotalVotos")
        geolocalizacionVotos = memcache.get(self.key+"Geolocalizacion")
        if votos is None:
            votos = {}
            self.totalVotos = 0
            geolocalizacionVotos = {}
            for censo in self.censos:
                escrutinios = model.Escrutinio.all()
                escrutinios.filter("censo  =",censo)
                for escrutinio in escrutinios:
                    if (not escrutinio.partido in votos):
                        votos[escrutinio.partido] = escrutinio.votos
                        geolocalizacionVotos[escrutinio.partido] = []
                    else:
                        votos[escrutinio.partido] += escrutinio.votos
                        geolocalizacionVotos[escrutinio.partido] += [[censo.provincia,escrutinio.votos]]
                    self.totalVotos += escrutinio.votos
            memcache.add(self.key+"VotosCandidaturas",votos)
            memcache.add(self.key+"TotalVotos",self.totalVotos)
            memcache.add(self.key+"Geolocalizacion",geolocalizacionVotos)

        candidaturas = self.candidaturasMayoritarias(votos)
        diputados = self.asignarDiputados(candidaturas, parlamento.asientosLibres)

        # Asignar diputados
        while (parlamento.asientosLibres > 0):
            diputado = diputados.pop()
            parlamento.anadirDiputados(diputado)

        parlamento.geolocalizar(geolocalizacionVotos)

        return parlamento

    # Devuelve la lista de candidaturas que alcanzan el porcentaje
    # minimo establecido por la ley d'Hont
    def candidaturasMayoritarias(self, votos):
        if self.pucherazo is not None:
            #print "Dando pucherazo!"
            votosBlanco = self.totalVotosBlanco
            votos = self.pucherazo.darPucherazo(votos,votosBlanco,self.caciques)
        candidaturasValidas = {}
        #print "Votos en ", censoProvincia.provincia
        for partido in votos:
            if ((1.0*votos[partido]/self.totalVotos) > self.threshold):
                candidaturasValidas[partido] = votos[partido]
        return candidaturasValidas


    # Calcula los coeficientes de cada candidatura
    def asignarDiputados(self, candidaturas,numDiputados):
        diputados = []
        # Divide los votos entre el numero de diputados
        for partido in candidaturas:
            votos = candidaturas[partido]
            for i in range(1,numDiputados+1):
                diputados += [(1.0*votos/i,partido)]

        # Reordena los votos obtenidos
        diputados.sort()
        #print "Diputados por provincia"
        #print diputados
        return diputados
