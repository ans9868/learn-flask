import os

class Config(object):
    SECRET_KEY = os.environ.get("secrete_key") or "you-will-never-guess"
