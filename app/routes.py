from app import app
from flask import render_template


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

