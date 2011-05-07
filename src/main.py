# -*- coding: utf-8 -*-
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

years_avaliable = [2004, 2008, 2012 ]
path = os.path.join(os.path.dirname(__file__), 'index.html')
        
class MainPage(webapp.RequestHandler):
    def get(self):
        year = self.request.get('year')
        algorithm = self.request.get('alg', 'dhont')
        # Read the avaliable years form database
        
        template_values = { 'years': years_avaliable,
                            'selected_year': year,
                            'alg': algorithm,
                            }
        self.response.out.write( template.render(path, template_values) )



application = webapp.WSGIApplication(
     [('/', MainPage)], debug = True)
run_wsgi_app(application)
