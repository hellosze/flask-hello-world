from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/backwards/<input>')
def get_backward(input):
    return input[::-1]
