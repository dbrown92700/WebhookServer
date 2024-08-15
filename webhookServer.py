# app.py

from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("\nData received from Webhook is:\n\n", json.dumps(request.json, indent=2))
        return "Webhook received!"

@app.route('/', methods = ['GET'])
def get_request():
    return('Up and running!')

host = input('What is your server IP? ')
app.run(host=host, port=8000)
