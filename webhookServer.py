# app.py

from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)
        return "Webhook received!"

@app.route('/', methods = ['GET'])
def get_request():
    return('Up and running!')

app.run(host='192.168.1.59', port=8000)
