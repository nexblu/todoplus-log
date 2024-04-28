import mongoengine as me
import datetime


class TaskLog(me.Document):
    username = me.StringField(required=True)
    log = me.StringField(required=True)
    created_at = me.FloatField(
        default=datetime.datetime.now(datetime.timezone.utc).timestamp()
    )
