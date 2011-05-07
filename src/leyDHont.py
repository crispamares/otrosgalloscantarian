import model
import math
from parlamento import *



class LeyDHont:
    def __init__(self, ano):
        self.diputadosProvincias = {}
        self.threshold = 0.03
        self.censos = model.CensoElectoral.all()
        self.censos.filter("ano =",ano)

    def repartirEscanos(self):
        parlamento = Parlamento(350)

        diputadosProvinciales = {}

        # Asignar diputados fijos de las provincias
        poblacionDeDerecho = 0
        for censoProvincia in self.censos:
            provincia = censoProvincia.provincia
            poblacionDeDerecho += censoProvincia.censoTotal
            candidaturas = self.candidaturasMayoritarias(censoProvincia)
            diputadosProvinciales[provincia] = self.asignarDiputados(candidaturas)
            #print "Diputados Provinciales"
            #print diputadosProvinciales[provincia]

            # Se elijen dos diputados de cada provincia a excepcion de ceuta y melilla
            diputado = diputadosProvinciales[provincia].pop()
            parlamento.anadirDiputados(diputado)
            if (provincia != "Ceuta" and provincia != "Melilla"):
                diputado = diputadosProvinciales[provincia].pop()
                parlamento.anadirDiputados(diputado)

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
                numDiputadosPorPoblacion -= 1

        # Asignar los diputados restantes segun coeficientes
        coeficientes.sort()
        while (parlamento.asientosLibres > 0):
            (coef,provincia) = coeficientes.pop()
            diputado = diputadosProvinciales[provincia].pop()
            parlamento.anadirDiputados(diputado)

        return parlamento


    # Devuelve la lista de candidaturas que alcanzan el porcentaje
    # minimo establecido por la ley d'Hont
    def candidaturasMayoritarias(self, censoProvincia):
        escrutinios = model.Escrutinio.all()
        escrutinios.filter("censo  =",censoProvincia)
        candidaturas = {}
        totalVotos = censoProvincia.votosTotales
        for escrutinio in escrutinios:
            if ((1.0*escrutinio.votos/totalVotos) > self.threshold):
                candidaturas[escrutinio.partido] = escrutinio.votos
        #print "+++++++++++++++++++++++++++++++"
        #print censoProvincia.provincia, "=>", candidaturas
        return candidaturas


    # Calcula los coeficientes de cada candidatura
    def asignarDiputados(self, candidaturas):
        numDiputados = 10 #numDiputados(provincia)
        diputados = []
        # Divide los votos entre el numero de diputados de la provincia
        for partido in candidaturas:
            votos = candidaturas[partido]
            for i in range(1,numDiputados+1):
                diputados += [(1.0*votos/i,partido)]

        # Reordena los votos obtenidos
        diputados.sort()
        return diputados
