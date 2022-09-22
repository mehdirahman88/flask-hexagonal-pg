import os

from src.main import APPNAME
from src.main.app import create_app

app = create_app(APPNAME, os.getenv("FLASK_ENV"))
