import mongoengine as me


class TaskLog(me.Document):
    username = me.StringField(required=True)
    log = me.StringField(required=True)
    created_at = me.FloatField(required=True)
