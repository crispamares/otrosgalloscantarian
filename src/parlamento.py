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
        elif partido == "I.U.":
            color = [66,169,25]
        elif partido == "C's":
            color = [255,110,45]
        elif partido == "CiU":
            color = [252,216,3]
        elif partido == "ESQUERRA":
            color = [238,171,80]
        elif partido == "EAJ-PNV" or partido == "PNV":
            color = [42,133,81]
        elif partido == "Libres":
            color = [255,255,255]
        elif partido == "B.N.G.":
            color = [148,187,225]
        elif partido == "CC-PNC":
            color = [4,116,190]
        elif partido == "VERDES":
            color = [34,132,29]            
        else:
            color = [random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)]
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
