from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import model
import os

loaded = False

class MainPage(webapp.RequestHandler):
  def get(self):
    #self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello, Gallo!!<br />')
    censos = model.CensoElectoral.all()
    censos.filter("comunidad =","Castilla - La Mancha")
    for censo in censos:
        self.response.out.write("<b>" + censo.comunidad + ":")
        self.response.out.write(censo.provincia + " Num. Habitantes: ")
        self.response.out.write(censo.poblacion)
        self.response.out.write("</b> <br />")
        escrutinios = model.Escrutinio.all()
        escrutinios.filter("censo  =",censo)
        for escrutinio in escrutinios:
            self.response.out.write("    " + escrutinio.partido + "=>")
            self.response.out.write(escrutinio.votos)
            self.response.out.write("<br />")

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
