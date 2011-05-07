from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import model
import os

loaded = False

class MainPage(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello, Gallo, Año Alegr&iacute;a!!\n')
    censos = model.CensoElectoral.all()
    #censos.filer('municipio=','Adra')
    for censo in censos:
        self.response.out.write(censo.comunidad + ":")
        self.response.out.write(censo.provincia + ":")
        self.response.out.write(censo.municipio + "\n")

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
