# import os
from flask import Flask
app = Flask(__name__)



@app.route('/')
def hello():
    '''Health check'''
    return "Hello World(V2)!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)