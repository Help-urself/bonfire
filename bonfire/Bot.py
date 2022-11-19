from flask import Flask
from flask import request
from flask import Response
import requests
app = Flask(__name__)
def Bots(TOKEN):
    return TOKEN

 

def edit_message(bot,chat_id,message_id,text):
            url = f'https://api.telegram.org/bot{bot}/editMessageText'
            payload = {
                'chat_id': chat_id,
                'message_id': message_id,
                'text': text,
                }
   
            r = requests.post(url,json=payload)
            return r

def commands(app):
    a=app.route('/',methods=['GET', 'POST'])
    return a
def run (app):
    """start flask server"""
    a=app.run(port=8080,host="0.0.0.0",debug=True)
    return a
