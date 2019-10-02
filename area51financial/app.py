
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask,render_template,request, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
import json
import pandas as pd
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/area51financial')
testing = engine.execute("SELECT * FROM history")
for record in testing:
    print(record)

@app.route("/")
def index():
    return render_template('area51financial.html')

@app.route("/results")
def results():
    return render_template('area51financial.html')

if __name__ == '__main__':
    app.run(debug=True)
