import flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from routes.task_log import task_log_router
from configs import debug_mode, database_url, database_name

db = MongoEngine()
app = flask.Flask("todoplus")
app.config["MONGODB_SETTINGS"] = {
    "db": database_name,
    "host": database_url,
}
db.init_app(app)
CORS(app, supports_credentials=True)

app.register_blueprint(task_log_router)

if __name__ == "__main__":
    app.run(debug=debug_mode)
