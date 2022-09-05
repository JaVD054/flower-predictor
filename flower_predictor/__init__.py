from flask import Flask,request, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'flower_predictor/static/uploads/'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"

db = SQLAlchemy(app)

from flower_predictor import route


