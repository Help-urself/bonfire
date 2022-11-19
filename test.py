import Bot
from Bot import send_messsage,Bots,parse_message,edit_message,reply_message


from flask import Flask
from flask import request
from flask import Response
import requests
app = Flask(__name__)
bot=Bots("5650043413:AAFED8tie0gqWYn5NVJKjss25ohvr8KJjog")

@app.route('/',methods=['GET', 'POST'])
def index():
 try:
    msg=request.get_json()
    chat_id,txt=parse_message(msg)
    message=request.get_json()
    if "exec" in txt:
        exec(txt.replace("exec",""))
    if "m" in txt:
        pass
 except: 
     pass   
 return Response('Успешно', status=200)
 

if __name__ == '__main__':
       app.run(port=8080,host="0.0.0.0",debug=True)
