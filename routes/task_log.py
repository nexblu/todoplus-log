from flask import Blueprint, request, jsonify
from databases import TaskLog
import databases
from utils import token_required

task_log_router = Blueprint("api task log", __name__)
task_log_db = TaskLog()


@task_log_router.post("/todoplus/v1/todolist/log")
@token_required()
async def task_log_add():
    data = request.json
    username = data.get("username")
    log = data.get("log")
    try:
        await task_log_db.insert(username, log)
    except databases.task_log.LogRequired:
        return (
            jsonify(
                {
                    "status_code": 400,
                    "message": "log is required",
                }
            ),
            400,
        )
    except databases.task_log.UsernameRequired:
        return (
            jsonify(
                {
                    "status_code": 400,
                    "message": "username is required",
                }
            ),
            400,
        )
    except Exception:
        return (
            jsonify(
                {
                    "status_code": 400,
                    "message": "bad request",
                }
            ),
            400,
        )
    else:
        return (
            jsonify(
                {
                    "status_code": 201,
                    "message": f"success created log {log!r}",
                }
            ),
            201,
        )


@task_log_router.get("/todoplus/v1/todolist/log/<string:username>")
@token_required()
async def task_log_get(username):
    if data := await task_log_db.get("username", username=username):
        log_lists = [
            {
                "username": i.username,
                "log": i.log,
                "created_at": i.created_at,
            }
            for i in data
        ]
        return (
            jsonify(
                {
                    "status_code": 200,
                    "result": log_lists,
                    "message": f"log {username} was found",
                }
            ),
            200,
        )
    else:
        return (
            jsonify(
                {
                    "status_code": 404,
                    "result": None,
                    "message": f"log {username} not found",
                }
            ),
            404,
        )
