from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import model
import leyDHont
import os

loaded = False

class MainPage(webapp.RequestHandler):
  def get(self):
    #self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello, Gallo!!<br />')
    censos = model.CensoElectoral.all()
    censos.filter("comunidad =","Catalu&ntilde;a")
    for censo in censos:
        self.response.out.write("<b>" + censo.comunidad + ":")
        self.response.out.write(censo.provincia + " Votos Totales: ")
        self.response.out.write(censo.votosTotales)
        self.response.out.write("</b> <br />")
        escrutinios = model.Escrutinio.all()
        escrutinios.filter("censo  =",censo)
        for escrutinio in escrutinios:
            self.response.out.write("    " + escrutinio.partido + "=>")
            self.response.out.write(escrutinio.votos)
            self.response.out.write("<br />")
    ley = leyDHont.LeyDHont(2008)
    parlamento = ley.repartirEscanos()
    print parlamento.distribucion['parties']
    print parlamento.distribucion['color']
    print parlamento.distribucion['seats']
    print parlamento.distribucion['total_seats']
    #self.response.out.write(parlamento.distribucion['parties'][0])

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
