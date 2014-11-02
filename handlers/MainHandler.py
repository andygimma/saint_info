import os
import jinja2
import webapp2

from AuthenticationHandler import AuthenticationHandler
from models import calls_db

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname( __file__ ), '..', 'templates')))

TEMPLATE = JINJA_ENVIRONMENT.get_template('index.html')

class MainHandler(AuthenticationHandler):
  def get(self):
    user = self.session.get('user')
    template_values = {
      'user': user
    }
    
    #e = event_db.Event(name = "North Central Victorian Floods",
                       #case_label = "A",
                       #short_name = "ncv_floods")
    #e.put()
    
    self.response.write(TEMPLATE.render(template_values))