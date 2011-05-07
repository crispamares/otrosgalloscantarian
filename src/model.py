from google.appengine.ext import db

class CensoElectoral(db.Model):
    ano = db.StringProperty()
    comunidad = db.StringProperty()
    provincia = db.StringProperty()
    poblacion = db.IntegerProperty()
    censoTotal = db.IntegerProperty()
    votosTotales = db.IntegerProperty()
    votosValidos = db.IntegerProperty()
    votosCandidatura = db.IntegerProperty()
    votosBlanco = db.IntegerProperty()
    votosNulo = db.IntegerProperty()

class Escrutinio(db.Model):
    censo = db.ReferenceProperty(CensoElectoral)
    partido = db.StringProperty()
    votos = db.IntegerProperty()
