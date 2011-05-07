import model
from parlamento import *

class LeyProporcional:
    def __init__(self,ano):
        self.censos = model.CensoElectoral.all()
        self.censos.filter("ano =","2008")

    def repartirEscanos(self):
        parlamento = Parlamento(350)

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

        # Repartir votos proporcionalmente
        for partido in votos:
            numDiputados = round(1.0 * votos[partido] * parlamento.asientosLibres / totalVotos);
            if (numDiputados > 0):
                parlamento.anadirDiputados(("fake",partido),numDiputados)

        return parlamento




