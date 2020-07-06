from flask import Flask

import mylib


app = Flask(__name__)

@app.route('/')
def main():
    return mylib.get_result('Hello!')
