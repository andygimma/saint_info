import os
import jinja2
import webapp2
import csv

from AuthenticationHandler import AuthenticationHandler

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname( __file__ ), '..', 'templates')))

TEMPLATE = JINJA_ENVIRONMENT.get_template('csv.html')

class CSVHandler(AuthenticationHandler):
  def get(self):
    user = self.session.get('user')
    template_values = {
      'user': user
    }
    self.response.write(TEMPLATE.render(template_values))
    self.response.headers['Content-Type'] = 'text/csv'
    self.response.headers['Content-Disposition'] = 'attachment; filename=file.csv'
    writer = csv.writer(self.response.out)
