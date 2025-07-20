import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "default_secret"
    UPLOAD_FOLDER = "uploads/"
    GENERATED_FOLDER = "generated/"
