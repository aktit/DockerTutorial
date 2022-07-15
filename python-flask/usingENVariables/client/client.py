from flask import Flask, render_template
import requests
import os
app = Flask(__name__)

@app.route('/')
def hello():
    try:
        x = requests.get("http://{flaskapi}:5000")
        return render_template('index.html', data = x.json())
    except:
        return render_template('index.html', data = 'API server is Down')

app.run(host='0.0.0.0',port=10000)





