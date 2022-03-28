from . import db


class Configuration(db.Document):
    _id = db.ObjectIdField()
    name = db.StringField(required=True, unique=True)
    description = db.StringField(default="")
    dateCreated = db.DateTimeField()
    dateModified = db.DateTimeField()
    showOnAdmin = db.BooleanField(default=False)


class PInfo(db.Document):
    _id = db.ObjectIdField()
    name = db.StringField(required=True, unique=True)
    info = db.StringField(required=True)
    # TODO: UI control for visualization
    control_type = db.StringField(choices=())


class PValue(db.Document):
    _id = db.ObjectIdField()
    pinfo = db.ReferenceField(PInfo)
    value = db.DynamicField(required=True)
    config = db.ReferenceField(Configuration)
    meta = {
        'indexes': [
            {'fields': ('pinfo', 'config'), 'unique': True}
        ]
    }

