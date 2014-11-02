import webapp2

from AuthenticationHandler import AuthenticationHandler

class LogoutHandler(AuthenticationHandler):
  def get(self):
    if self.session.get('user'):
      del self.session['user']
    self.redirect("/")