
from flask import Flask,render_template,request, url_for, jsonify, redirect
import pandas as pd
import requests
import os
import psycopg2

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

    items = jsonify(dependents,checkingAcctBalance,loanLength,creditHistory,loanPurpose,loanSize,savingsAcctBalance,employmentHistory,cosignerCoborrower,age,otherLoans,homeowner,employmentType,telephone,foreignWorker)

    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("CREATE TABLE area51financial (id serial PRIMARY KEY, i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15)")
    cur.execute("INSERT INTO area51financial (id serial PRIMARY KEY, i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15), VALUES (dependents,checkingAcctBalance,loanLength,creditHistory,loanPurpose,loanSize,savingsAcctBalance,employmentHistory,cosignerCoborrower,age,otherLoans,homeowner,employmentType,telephone,foreignWorker)")
    conn.commit()
    cur.close()
    conn.close()

    return items

@app.route("/submit", methods = ['POST','GET'])
def test():
    return 
if __name__ == '__main__':
    app.run(debug=True)
