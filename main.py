import os
from flask import Flask
app = Flask(__Name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/status')
def hello():
    return 'I am good'

if __name__ == "__main__":
    app.run(host="0.0.0.0.", port=8080)
