from flower_predictor import app
from flask import render_template


@app.route('/')
def hlo_world():
    return render_template("index.html")


