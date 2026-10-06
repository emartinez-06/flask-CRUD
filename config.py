import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DB_HOST = "127.0.0.1"
    DB_USER = "eim"
    DB_NAME = "flask_app"
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
