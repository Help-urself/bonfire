import os
import sys
sys.path.append(os.path.abspath('your campfire folder path'))
from Bot import Bots,edit_message,commands,run
from flask import Flask
from method import *
import time
from flask import request,Response
import requests
app = Flask(__name__)
bot=Bots("TOKEN")#setting up a token for requests

@commands(app)#message handler
def main():#the main name can be anything, it doesn't matter
 try:
    message=request.get_json()#receive a message
    chat_id,text,message_id,message_author_username,message_author_id,message_author_is_bot,message_author_first_name,message_author_language_code,message_date=parse_message(message=message)#methods message
    if "/start" in text: #/start command handler
     reply_message(bot,msg_id=message_id,chat_id=chat_id,text="відповідь ._.")
#з parse_mode
     reply_message(bot,msg_id=message_id,chat_id=chat_id,text="<b>відповідь жирним шрифтом .-.</b>",parse_mode="HTML")#робимо текст жирним шрифтом 
 except Exception as error:
     print(error)
 return Response('OK', status=200)#return to cmd (POST/ 200 OK)

if __name__ == '__main__':
       run(app)#app.run(port=8080,host="0.0.0.0",debug=True)