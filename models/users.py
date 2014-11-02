from google.appengine.ext import db

class User(db.Model):
    email = db.StringProperty()
    password = db.StringProperty()



    def authenticate(self, email, password):
        raise Exception(email)