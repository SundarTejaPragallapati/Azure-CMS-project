import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    # ---------- Flask ----------
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # ---------- Azure Blob Storage ----------
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsstorage12345'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # ---------- Azure SQL Database ----------
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms-sql-server-123.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')

    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://"
        + SQL_USER_NAME + ":" + (SQL_PASSWORD or "")
        + "@"
        + SQL_SERVER + ":1433/"
        + SQL_DATABASE
        + "?driver=ODBC+Driver+18+for+SQL+Server"
        + "&Encrypt=yes"
        + "&TrustServerCertificate=no"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ---------- Microsoft Entra ID Login ----------
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    CLIENT_ID = os.environ.get("CLIENT_ID") or "aaeca545-46a0-41ba-82b0-961cf4843a8d"
    AUTHORITY = "https://login.microsoftonline.com/common"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"