from google.appengine.ext import db

class Call(db.Model):
    phone_number = db.StringProperty()
    town = db.StringProperty()
    community = db.StringProperty()
    symptoms = db.BooleanProperty()
    admitted = db.BooleanProperty()
    turned_away = db.BooleanProperty
    caring_for_someone = db.BooleanProperty()
    been_in_contact_with_deceased = db.BooleanProperty()
    private_toilet = db.BooleanProperty()
    purified_cleaning_water = db.BooleanProperty()
    purified_drinking_water = db.BooleanProperty()
    disinfectants = db.BooleanProperty()
    hunt = db.BooleanProperty()
    eat_bush_meat = db.BooleanProperty()
    designated_trash_area = db.BooleanProperty()
    fever = db.BooleanProperty()
    vomiting_toileting = db.BooleanProperty()
    unusual_bleeding = db.BooleanProperty()
    headaches = db.BooleanProperty()
    joint_muscle_pain_weakness = db.BooleanProperty()
    sore_throat = db.BooleanProperty()
