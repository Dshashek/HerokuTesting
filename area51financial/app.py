
from flask import Flask,render_template,request, url_for, jsonify, redirect
import pandas as pd
import requests
import os
import psycopg2
from Python_Functions import parse_input

def parse_input(list):
    input = pd.DataFrame(list)

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    return render_template('area51financial.html')

@app.route("/submit", methods = ['POST','GET'])
def submit():
    dependents = request.form.get('dependents')
    checkingAcctBalance = request.form.get('checkingAcctBalance')
    loanLength = request.form.get('loanLength')
    creditHistory = request.form.get('creditHistory')
    loanPurpose = request.form.get('loanPurpose')
    loanSize = request.form.get('loanSize')
    savingsAcctBalance = request.form.get('savingsAcctBalance')
    employmentHistory = request.form.get('employmentHistory')
    cosignerCoborrower = request.form.get('cosignerCoborrower')
    age = request.form.get('age')
    otherLoans = request.form.get('otherLoans')
    homeowner = request.form.get('homeowner')
    employmentType = request.form.get('employmentType')
    telephone = request.form.get('telephone')
    foreignWorker = request.form.get('foreignWorker')   

    items = [dependents,checkingAcctBalance,loanLength,creditHistory,loanPurpose,loanSize,savingsAcctBalance,employmentHistory,cosignerCoborrower,age,otherLoans,homeowner,employmentType,telephone,foreignWorker]

    parse_input(items)

    return redirect('/', code=302)

@app.route("/submit", methods = ['POST','GET'])
def test():
    return 
if __name__ == '__main__':
    app.run(debug=True)
