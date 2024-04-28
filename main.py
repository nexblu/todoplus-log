import flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from routes.task_log import task_log_router
from config import debug_mode, mongodb_url, database_name, port
from databases import db_session
from utils import handle_404, handle_415, handle_429, handle_400

db = MongoEngine()
app = flask.Flask("todoplus")
app.config["MONGODB_SETTINGS"] = {
    "db": database_name,
    "host": mongodb_url,
}
db.init_app(app)
CORS(app, supports_credentials=True)

app.register_blueprint(task_log_router)
app.register_error_handler(429, handle_429)
app.register_error_handler(404, handle_404)
app.register_error_handler(415, handle_415)
app.register_error_handler(400, handle_400)


@app.after_request
async def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response


@app.teardown_appcontext
async def shutdown_session(exception=None):
    db_session.remove()


@app.get("/")
def home():
    return "welcome to todoplus log"


if __name__ == "__main__":
    app.run(debug=debug_mode, port=port)
