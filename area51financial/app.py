
from flask import Flask,render_template,request, url_for, jsonify, redirect
import pandas as pd
import requests
import os
import psycopg2
from tensorflow.keras.models import load_model

def parse_input(list):
    input = pd.DataFrame(list)
    print(list)

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    return render_template('area51financial.html')

@app.route("/submit", methods = ['POST','GET'])
def submit():
    loanLength = request.form.get('loanLength')
    loanPurpose = request.form.get('loanPurpose')
    loanSize = request.form.get('loanSize')
    employmentHistory = request.form.get('employmentHistory')
    cosignerCoborrower = request.form.get('cosignerCoborrower')
    age = request.form.get('age')
    homeowner = request.form.get('homeowner')
    employmentType = request.form.get('employmentType')
    telephone = request.form.get('telephone')


    items = [loanLength,loanPurpose,loanSize,employmentHistory,cosignerCoborrower,age,homeowner,employmentType,telephone]

    parse_input(items)

    return redirect('/', code=302)

@app.route("/submit", methods = ['POST','GET'])
def test():
    return 
if __name__ == '__main__':
    app.run(debug=True)
