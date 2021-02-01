from flask import Flask
from helper import pets

app = Flask(__name__)

app.debug = True

@app.route('/')
def index():
    return "<h1>Adopt a Pet!</h1>"

