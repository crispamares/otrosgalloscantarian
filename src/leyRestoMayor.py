import model
from parlamento import *
from google.appengine.api import memcache

class LeyRestoMayor:
    def __init__(self,ano,cociente):
        self.censos = model.CensoElectoral.all()
        self.censos.filter("ano =",ano)
        self.key = "VotosNacionales"+ano

        self.cociente = None
        if cociente == 'Hare':
            self.cociente = self.Hare
        elif cociente == 'Droop':
            self.cociente = self.Droop
        elif cociente == 'Imperiali':
            self.cociente = self.Imperiali


    def Droop(self,votos,escanos):
         return 1 + (votos / (escanos+1))

    def Hare(self,votos,escanos):
         return votos / escanos

    def Imperiali(self,votos,escanos):
         return votos / (escanos+2)


    def repartirEscanos(self):
        parlamento = Parlamento(350)

        votos = memcache.get(self.key+"VotosCandidaturas")
        totalVotos = memcache.get(self.key+"TotalVotos")
        geolocalizacionVotos = memcache.get(self.key+"Geolocalizacion")
        if votos is None:
            votos = {}
            totalVotos = 0
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
                    totalVotos += escrutinio.votos
            memcache.add(self.key+"VotosCandidaturas",votos)
            memcache.add(self.key+"TotalVotos",totalVotos)
            memcache.add(self.key+"Geolocalizacion",geolocalizacionVotos)
        #print "Geolocalizacion"
        #print geolocalizacionVotos['CiU']

        # Calcular cociente
        q = self.cociente(totalVotos,parlamento.asientosLibres)
        #print "Cociente", q

        # Repartir votos proporcionalmente
        restos = []
        for partido in votos:
            numDiputados = round(votos[partido] / q)
            Ri = votos[partido] - q*numDiputados
            restos += [(Ri,partido)]
            if (numDiputados > 0):
                parlamento.anadirDiputados(("fake",partido),numDiputados)

        # Asignar restos
        restos.sort()
        while (parlamento.asientosLibres > 0):
            mejorResto = restos.pop()
            parlamento.anadirDiputados(("fake",mejorResto[1]),1);

        parlamento.geolocalizar(geolocalizacionVotos)

        return parlamento




