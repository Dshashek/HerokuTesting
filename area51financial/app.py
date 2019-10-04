
from flask import Flask,render_template,request, url_for, jsonify, redirect
import pandas as pd
import requests
import os
import psycopg2
from tensorflow.keras.models import load_model

def to_nn_inputs(input):


    input_options = ['A40','A41','A410','A42','A43','A44','A45','A46','A48','A49','A71','A72','A73','A74','A75','A101','A102','A103','A151','A152','A153','A191','A192','A201','A202','B10','B11','B12','B13','B14','B15','B20','B21','B22','B23','B24','B25','B26','B27','B30','B31','B32','B33','B34','B35']
    pd_proto = {}

    for item in input_options:
        pd_proto[f'{item}'] = 0

    df = pd.DataFrame(pd_proto,index=['input'])

    counter = 0

    while counter < len(input):
        df[f'{input[counter]}'] = df[f'{input[counter]}'] + 1
        counter = counter+1

    nn_inputs = df.values.tolist()[0]

    return print(nn_inputs)

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
    telephone = request.form.get('telephone')
    foreignworker = request.form.get('foreignWorker')

    items = [loanLength,loanPurpose,loanSize,employmentHistory,cosignerCoborrower,age,homeowner,telephone,foreignworker]

    to_nn_inputs(items)

    return redirect('/', code=302)

@app.route("/submit", methods = ['POST','GET'])
def test():
    return 
if __name__ == '__main__':
    app.run(debug=True)
