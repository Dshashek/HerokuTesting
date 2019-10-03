
from flask import Flask,render_template,request, url_for
import pandas as pd
import requests
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('area51financial.html')

@app.route('/receiver', methods = ['POST'])
def worker():
	# read json + reply
	data = request.get_json()
	result = ''

	for item in data:
		# loop over every row
		result += str(item['make']) + '\n'

	return result

@app.route("/results")
def results():
    return render_template('area51financial.html')

if __name__ == '__main__':
    app.run(debug=True)
