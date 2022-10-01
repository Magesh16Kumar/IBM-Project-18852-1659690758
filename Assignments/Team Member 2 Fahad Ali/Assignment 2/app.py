from re import L
from requests import post
from flask import Flask

app = Flask(__name__)

@app.get('/')
def get_method():
    return 'You have invoked GET HTTP method'

@app.put('/')
def put_method():
    return 'You have invoked PUT HTTP method'

@app.delete('/')
def delete_method():
    return 'You have invoked DELETE HTTP method'

@app.post('/')
def post_method():
    return 'You have invoked POST HTTP method'