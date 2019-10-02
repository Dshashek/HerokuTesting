

# coding: utf-8

# In[1]:


from flask import Flask,render_template,request

import pandas as pd

app = Flask(__name__)
   

@app.route("/")
def index():
    return render_template('Index.html')


if __name__ == '__main__':
    app.run(debug=False)
