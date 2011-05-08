import model
from parlamento import *
from google.appengine.api import memcache

class LeyProporcional:
    def __init__(self,ano):
        self.censos = model.CensoElectoral.all()
        self.censos.filter("ano =",ano)
        self.key = "LeyProporcional"+ano

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

        # Repeartir votos proporcionalmente
        totalEscanos = parlamento.asientosLibres
        for partido in votos:
            numDiputados = round(1.0 * votos[partido] * totalEscanos / totalVotos);
            if (numDiputados > 0):
                parlamento.anadirDiputados(("fake",partido),numDiputados)
        
        parlamento.anadirDiputados((None,"Libres"), parlamento.asientosLibres)               

        return parlamento




