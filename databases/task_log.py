from .database import Database
from models import TaskLog as Tl


class TaskLog(Database):
    def __init__(self) -> None:
        super().__init__()

    async def insert(self, username, log, created_at):
        task_log = Tl(username=username, log=log, created_at=created_at)
        task_log.save()

    async def delete(self):
        pass

    async def get(self):
        pass

    async def update(self):
        pass
