import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    # ---------- Flask ----------
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # ---------- Azure Blob Storage ----------
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsstorage12345'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # ---------- DATABASE (SAFE VERSION FOR AZURE) ----------
    # Use SQLite on cloud to avoid SQL Server driver issues
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///site.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ---------- Microsoft Entra ID Login ----------
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    CLIENT_ID = os.environ.get("CLIENT_ID") or "aaeca545-46a0-41ba-82b0-961cf4843a8d"
    AUTHORITY = "https://login.microsoftonline.com/common"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]

    # ---------- Session ----------
    SESSION_TYPE = "filesystem"