# Building the API in Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) # wrap our app in cors 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app) # gives access to the database url above
