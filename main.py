# -*- coding: utf-8 -*-
import sys
import os

ROOT = os.path.dirname(__file__)
INDEX_PATH = os.path.join(ROOT, 'views', 'index.html')

sys.path.append(os.path.join(ROOT, "src"))


import model
import simplejson

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import memcache

from leyDHont import LeyDHont
from leyProporcional import LeyProporcional
from leyCoefienteDroop import LeyCoeficienteDroop
from pucherazo import Pucherazo
# TODO sacar una lista de los años existentes ...
years_avaliable = [2008, 2004, 2000, 1996 ]


def getElementCached(nombreLey, year, leyElectoral):
  key = nombreLey+year
  parlamento = memcache.get(key)
  if parlamento is not None:
    return parlamento
  else:
    ley = leyElectoral(year)
    parlamento = ley.repartirEscanos()
    memcache.add(key, parlamento)
    return parlamento
    

class MainPage(webapp.RequestHandler):

  def get(self):
    # If there is GET/POST data, retrieve it
    year = self.request.get('year', "")
    algorithm = self.request.get('alg', "")
    param = self.request.get('param',"")
    flush_cache = self.request.get('flushcache', False)
    hacerPucherazo = self.request.get('pucherazo',False)
    caciques = self.request.get('caciques',"")

    if flush_cache:
        memcache.flush_all()

    # Read the avaliable years form model
    model.CensoElectoral.all()
    template_values = { 'years': years_avaliable,
            'selected_year': year,
            'alg': algorithm,
            }

    pucherazo = None
    if hacerPucherazo == "True":
        pucherazo = Pucherazo()

    if( algorithm == 'dhont'):
      params = param.split(":")
      th = 0.03
      if param != "":
          th = eval(params[0])

      ley = LeyDHont(year,th)
      ley.manipular(caciques.split(":"),pucherazo)
      parlamento = ley.repartirEscanos()
      self.response.out.write( simplejson.dumps(parlamento.configuracion()) )
    elif(algorithm == 'manoli'):
      ley = LeyProporcional(year)
      parlamento = ley.repartirEscanos()
      self.response.out.write( simplejson.dumps(parlamento.configuracion()) )
    elif(algorithm == 'droop'):
      ley = LeyCoeficienteDroop(year)
      parlamento = ley.repartirEscanos()
      self.response.out.write( simplejson.dumps(parlamento.configuracion()) )
    else:
      self.response.out.write( template.render(INDEX_PATH, template_values) )



application = webapp.WSGIApplication(
     [('/', MainPage),
      ],
      debug = True)
run_wsgi_app(application)
