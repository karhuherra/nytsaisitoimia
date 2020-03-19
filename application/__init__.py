from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tyoaikaseuranta.db"

app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views

from application.tyoaikaseuranta.tyontekijat import models
from application.tyoaikaseuranta.tyontekijat import views
from application.tyoaikaseuranta.projektit import models
from application.tyoaikaseuranta.projektit import views


db.create_all()


