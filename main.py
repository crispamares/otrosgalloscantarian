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

from leyDHont import LeyDHont

years_avaliable = [2004, 2008, 2012 ]


class MainPage(webapp.RequestHandler):
  
  def get(self):
    # If there is GET/POST data, retrieve it
    year = self.request.get('year', "")
    algorithm = self.request.get('alg', "")
    
    # Read the avaliable years form model
    model.CensoElectoral.all()
    template_values = { 'years': years_avaliable,
            'selected_year': year,
            'alg': algorithm,
            }
    
    if( algorithm == 'dhont'):
      # TODO load from db
      ley = LeyDHont(year)
      parlamento = ley.repartirEscanos()            
      self.response.out.write( simplejson.dumps(parlamento.distribucion) )
    elif(algorithm == 'dhont2'):
      pass
    elif(algorithm == 'dhont3'):
      pass
          
    else:
      self.response.out.write( template.render(INDEX_PATH, template_values) )



application = webapp.WSGIApplication(
     [('/', MainPage),
      ],
      debug = True)
run_wsgi_app(application)
