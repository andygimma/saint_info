import os
import jinja2
import webapp2
from google.appengine.ext import db

from models import users
from AuthenticationHandler import AuthenticationHandler

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname( __file__ ), '..', 'templates')))

TEMPLATE = JINJA_ENVIRONMENT.get_template('login.html')

class LoginHandler(AuthenticationHandler):
  def get(self):
    if self.session.get('user'):
      del self.session['user']
    if not self.session.get('referrer'):
      self.session['referrer'] = \
	  self.request.environ['HTTP_REFERER'] \
	  if 'HTTP_REFERER' in self.request.environ \
	  else '/login'
    template_values = {}
     
    q = users.User.all()
    if q.count() == 0:
      user = users.User(email="LDSchurch", password="breezelock121")
      user.put()
    user = self.session.get('user')
    template_values = {
      'user': user
    }
    self.response.write(TEMPLATE.render(template_values))
    
  def post(self):
    email = self.request.get("email")
    password = self.request.get("password")
  
    q = users.User.all()
    q.filter('email =', email)
    q.filter('password =', password)
    user = q.get()
    
    if user:
      #pass
      self.session['user'] = user.email
      self.redirect("/lds-map")
    else:
      self.redirect("/logout")
 