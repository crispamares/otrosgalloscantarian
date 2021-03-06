import model
from parlamento import *
from google.appengine.api import memcache

class LeyCoeficienteDroop:
    def __init__(self,ano):
        self.censos = model.CensoElectoral.all()
        self.censos.filter("ano =",ano)
        self.key = "LeyCoeficienteDroop"+ano

    def repartirEscanos(self):
        parlamento = Parlamento(350)

        votos = memcache.get(self.key+"VotosCandidaturas")
        totalVotos = memcache.get(self.key+"TotalVotos")
        if votos is None:
            votos = {}
            totalVotos = 0
            for censo in self.censos:
                escrutinios = model.Escrutinio.all()
                escrutinios.filter("censo  =",censo)
                for escrutinio in escrutinios:
                    if (not escrutinio.partido in votos):
                        votos[escrutinio.partido] = escrutinio.votos
                    else:
                        votos[escrutinio.partido] += escrutinio.votos
                    totalVotos += escrutinio.votos
            memcache.add(self.key+"VotosCandidaturas",votos)
            memcache.add(self.key+"TotalVotos",totalVotos)

        # Coef Droop
        q = 1 + round((1.0*totalVotos) / (parlamento.asientosLibres+1.0))

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

        return parlamento




