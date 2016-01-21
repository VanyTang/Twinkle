from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'MONGO'

mongo = PyMongo(app)

SECRET_KEY = 'abcdefghijkmn'
app.secret_key = 'abcdefghijkmn'

from app import views
