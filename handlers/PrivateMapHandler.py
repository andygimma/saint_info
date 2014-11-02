import os
import jinja2
import webapp2

from AuthenticationHandler import AuthenticationHandler

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname( __file__ ), '..', 'templates')))

TEMPLATE = JINJA_ENVIRONMENT.get_template('private-map.html')

class PrivateMapHandler(AuthenticationHandler):
  def get(self):
    user = self.session.get('user')
    if not user:
      self.redirect("/login")
      return
    template_values = {
      'user': user
    }
    self.response.write(TEMPLATE.render(template_values))