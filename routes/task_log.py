from flask import Blueprint, request, jsonify
from databases import TaskLog

task_log_router = Blueprint("api task log", __name__)
task_log_db = TaskLog()


@task_log_router.post("/todoplus/v1/todolist/log")
async def task_log_add():
    data = request.json
    username = data.get("username")
    log = data.get("log")
    created_at = data.get("created_at")
    try:
        await task_log_db.insert(username, log, created_at)
    except:
        return (
            jsonify(
                {
                    "status_code": 400,
                    "result": "bad request",
                }
            ),
            400,
        )
    else:
        return (
            jsonify(
                {
                    "status_code": 201,
                    "result": f"success created log {log!r}",
                }
            ),
            201,
        )
