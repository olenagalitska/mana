from . import db


class Configuration(db.Document):
    name = db.StringField(required=True, unique=True)
    description = db.StringField(default="")
    dateCreated = db.DateTimeField()
    dateModified = db.DateTimeField()
    showOnAdmin = db.BooleanField(default=False)


class PInfo(db.Document):
    name = db.StringField(required=True, unique=True)
    info = db.StringField(required=True)
    # TODO: UI control for visualization
    control_type = db.StringField(choices=())


class PValue(db.Document):
    pinfo = db.ReferenceField(PInfo, required=True)
    value = db.DynamicField(required=True)
    config = db.ReferenceField(Configuration, required=True)
    meta = {
        'indexes': [
            {'fields': ('pinfo', 'config'), 'unique': True}
        ]
    }

