from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

from app.models import User

u = User(username='dimzhang', email='d@gmail.com')

print(u,u.id,u.username,u.email,u.password_hash)