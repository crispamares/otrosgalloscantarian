import random

class Parlamento:
    def __init__(self, numDiputados):
        self.distribucion = {'parties':[],'seats':[],'colors':[],'total_seats':numDiputados}
        self.escanos = {}
        self.asientosLibres = numDiputados
        
    def colorPartido(self, partido):
        color = []
        if partido == "UPyD":
            color = [229,0,131]
        elif partido == "P.S.O.E.":
            color = [237,27,36]
        elif partido == "P.P.":
            color = [0,163,224]
        else:
            color = [(len(partido)*3)%256,(self.escanos[partido]*len(partido))%256,255]
        return color

    def anadirDiputados(self, diputado, numDiputados=1):
        partido = diputado[1]
        if (not partido in self.escanos):
            self.escanos[partido] = numDiputados
        else:
            self.escanos[partido] += numDiputados
        self.asientosLibres -= numDiputados

    def configuracion(self):
        emparejados = []
        for partido in self.escanos:
            emparejados += [(self.escanos[partido],partido,self.colorPartido(partido))]
        emparejados.sort()
        emparejados.reverse()
        for i in range(0,len(emparejados)):
            self.distribucion['parties'] += [emparejados[i][1]]
            self.distribucion['seats'] += [emparejados[i][0]]
            self.distribucion['colors'] += [emparejados[i][2]]
        return self.distribucion
