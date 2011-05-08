import random

class Parlamento:
    def __init__(self, numDiputados):
        self.distribucion = {'parties':[],'seats':[],'colors':[],'total_seats':numDiputados}
        self.asientosLibres = numDiputados

    def anadirDiputados(self, diputado, numDiputados=1):
        partido = diputado[1]
        if (not partido in self.distribucion['parties']):
            self.distribucion['parties'] += [partido]
            self.distribucion['seats'] += [numDiputados]
            self.distribucion['colors'] += [[random.randint(0,255),random.randint(0,255),random.randint(0,255)]] # pedir a la bbdd
        else:
            index = self.distribucion['parties'].index(partido)
            self.distribucion['seats'][index] += numDiputados
        self.asientosLibres -= 1
