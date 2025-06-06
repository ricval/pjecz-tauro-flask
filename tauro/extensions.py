"""
Flask Extensions
"""

from flask_login import LoginManager
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from passlib.context import CryptContext
from flask_socketio import SocketIO

csrf = CSRFProtect()
database = SQLAlchemy()
login_manager = LoginManager()
moment = Moment()
pwd_context = CryptContext(schemes=["pbkdf2_sha256", "des_crypt"], deprecated="auto")
socketio = SocketIO(cors_allowed_origins="*")
