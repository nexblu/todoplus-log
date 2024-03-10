from dotenv import load_dotenv
import os

load_dotenv()

debug_mode = os.environ.get("DEBUG")
database_name = os.environ.get("DB_NAME")
database_url = os.environ.get("DB_URL")
