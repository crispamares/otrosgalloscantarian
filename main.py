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
    
    dataResponse = {}
    if( algorithm == 'dhont'):
      # TODO load from db
      color = [[255,0,0], [123,45,78], [0,0,255]]
      seats = [25, 75, 30]

      dataResponse.setdefault('color', color)
      dataResponse.setdefault('seats', seats)
      dataResponse.setdefault('total_seats', sum(seats))
      
      self.response.out.write( simplejson.dumps(dataResponse) )
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
