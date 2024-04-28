from dotenv import load_dotenv
import os

load_dotenv()

debug_mode = os.environ.get("DEBUG")
database_name = os.environ.get("DB_NAME")
mongodb_url = os.environ.get("MONGODB_URL")
port = os.environ.get("PORT")
jwt_key = os.environ.get("JWT_KEY")
algorithm = os.environ.get("ALGORITHM")
sql_url = os.environ.get("SQL_URL")
