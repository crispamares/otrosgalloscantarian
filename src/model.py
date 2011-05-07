from google.appengine.ext import db

class CensoElectoral(db.Model):
    ano = db.StringProperty()
    comunidad = db.StringProperty()
    provincia = db.StringProperty()
    municipio = db.StringProperty()
    poblacion = db.StringProperty()
    censoTotal = db.StringProperty()
    votosTotales = db.StringProperty()
    votosValidos = db.StringProperty()
    votosCandidatura = db.StringProperty()
    votosBlanco = db.StringProperty()
    votosNulo = db.StringProperty()

class Escrutinio(db.Model):
    censo = db.ReferenceProperty(CensoElectoral)
    partido = db.StringProperty()
    votos = db.StringProperty()
