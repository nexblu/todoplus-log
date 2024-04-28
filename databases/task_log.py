from .database import Database
from models import TaskLog as Tl


class UsernameRequired(Exception):
    def __init__(self, message="username is required"):
        self.message = message
        super().__init__(self.message)


class LogRequired(Exception):
    def __init__(self, message="log is required"):
        self.message = message
        super().__init__(self.message)


class TaskLog(Database):
    @staticmethod
    async def insert(username, log):
        if username_space := username.isspace() or not username:
            raise UsernameRequired
        if log_space := log.isspace() or not log:
            raise LogRequired
        task_log = Tl(username=username, log=log)
        task_log.save()

    @staticmethod
    async def delete():
        pass

    @staticmethod
    async def get(category, **kwargs):
        username = kwargs.get("username")
        if category == "username":
            log = Tl.objects(username=username).all()
            return log

    @staticmethod
    async def update():
        pass
