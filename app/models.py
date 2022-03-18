from . import db


class Configuration(db.Document):
    name = db.StringField(required=True)
    description = db.StringField(default="")
    dateCreated = db.DateTimeField(required=True)
    dateModified = db.DateTimeField()
    showOnAdmin = db.BooleanField(default=False)
