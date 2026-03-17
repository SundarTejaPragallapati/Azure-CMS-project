import os

class Config(object):

    # -------------------------------
    # 🔐 Flask Security
    # -------------------------------
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-key"


    # -------------------------------
    # 🗄️ Database (SQLite — safest for now)
    # Azure App Service persists ONLY /home
    # -------------------------------
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:////home/site/wwwroot/app.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # -------------------------------
    # 📦 Azure Blob Storage
    # Put your connection string in Azure App Settings
    # -------------------------------
    BLOB_CONNECTION_STRING = os.environ.get("BLOB_CONNECTION_STRING")

    BLOB_CONTAINER = os.environ.get("BLOB_CONTAINER") or "images"


    # -------------------------------
    # 🔐 Microsoft Entra ID (Azure AD Login)
    # -------------------------------
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

    AUTHORITY = "https://login.microsoftonline.com/common"

    REDIRECT_PATH = "/getAToken"

    SCOPE = ["User.Read"]


    # -------------------------------
    # 💾 Session
    # -------------------------------
    SESSION_TYPE = "filesystem"