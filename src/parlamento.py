import random

class Parlamento:
    def __init__(self, numDiputados):
        self.distribucion = {'parties':[],'places':[],'seats':[],'colors':[],'total_seats':numDiputados}
        self.escanos = {}
        self.asientosLibres = numDiputados
        self.geolocalizacion = None

    def geolocalizar(self, geolocalizacionVotos):
        self.geolocalizacion = geolocalizacionVotos

    def colorPartido(self, partido):
        color = []
        mayusculas = partido.upper()
        siglas = mayusculas.replace(".","")
        if siglas == "UPYD":
            color = [229,0,131]
        elif siglas.find("PSOE") >= 0:
            color = [237,27,36]
        elif siglas == "PP":
            color = [0,163,224]
        elif siglas == "IU.":
            color = [66,169,25]
        elif siglas == "C's":
            color = [255,110,45]
        elif siglas == "CiU":
            color = [252,216,3]
        elif siglas == "ESQUERRA":
            color = [238,171,80]
        elif siglas == "EAJ-PNV" or siglas == "PNV":
            color = [42,133,81]
        elif siglas == "Libres":
            color = [255,255,255]
        elif siglas == "BNG":
            color = [148,187,225]
        elif siglas == "CC-PNC":
            color = [4,116,190]
        elif siglas == "VERDES":
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

    def sanitize(self,provincia):
        prov = provincia.replace(' ','_')
        prov = prov.replace('/','-')
        while prov.find('&') >= 0:
            i = prov.find('&')
            prov = prov.replace(prov[i:i+1],'')
            j = prov.find(';')
            prov = prov.replace(prov[i+1:j+1],'')
        return prov

    def configuracion(self):
        emparejados = []
        for partido in self.escanos:
            provVotadas = self.geolocalizacion[partido]
            for i in range(0,len(provVotadas)):
                provVotadas[i][0] = self.sanitize(provVotadas[i][0])
            emparejados += [(self.escanos[partido],partido,self.colorPartido(partido),provVotadas)]

        emparejados.sort()
        emparejados.reverse()
        for i in range(0,len(emparejados)):
            self.distribucion['parties'] += [emparejados[i][1]]
            self.distribucion['seats'] += [emparejados[i][0]]
            self.distribucion['colors'] += [emparejados[i][2]]
            self.distribucion['places'] += [emparejados[i][3]]
        return self.distribucion
