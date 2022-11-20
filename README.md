# bonfire




bonfire this framework for [Telegram Bot API](https://core.telegram.org/bots/api) built on [flask](https://flask.palletsprojects.com/en/2.2.x/ ) and [requests](https://requests.readthedocs.io/en/latest/) <br>
**Ukrainian launge translate -> [click](https://github.com/Help-urself/bonfire/blob/main/Uk.md)**<br>
**instaling**
```python 
git clone https://github.com/Help-urself/bonfire
```
or

```python 
pip install -i https://test.pypi.org/simple/ bonfire-tg-libraly

```


## Examples
<details>
  <summary> Click </summary>


**1.install interceptor**
- install [ngrok](https://ngrok.com/) and start the server according to the instructions on the website.
- set webhook `https://api.telegram.org/botTOKEN/setWebhook?url=you url ngrok/hosting url`

### Simple [`send_message`](https://core.telegram.org/method/messages.sendMessage) request

```python
#git clone
import os
import sys
sys.path.append(os.path.abspath('your campfire folder path'))
import Bot
from Bot import Bots,commands,run
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
        send_message(bot=bot,chat_id=chat_id,text=f'hello @{message_author_username}!')#send message
 except Exception as error:
     print(error)
 return Response('OK', status=200)#return to cmd (POST/ 200 OK)

if __name__ == '__main__':
       run(app)#app.run(port=8080,host="0.0.0.0",debug=True)
```

```py
#pip install
from bonfire.Bot import Bots,commands,run
from flask import Flask
from bonfire.method import *
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
        send_message(bot=bot,chat_id=chat_id,text=f'hello @{message_author_username}!')#send message
 except Exception as error:
     print(error)
 return Response('OK', status=200)#return to cmd (POST/ 200 OK)

if __name__ == '__main__':
       run(app)#app.run(port=8080,host="0.0.0.0",debug=True)
       """set-webhook - > https://api.telegram.org/botTOKEN/setWebhook?url=URL"""
```

  </details>
  
## Documentation (in development)
<details>
  <summary> Click </summary>
  
  
### functions

**send_message**
  
```python 
def send_message(bot,chat_id,text):
  ```
  -**bot** - keyword where you store the token<br>
  -**chat_id** - you can use your chat id or use the chat_id method<br>
  -**text** - 
your message text<br>
  -**parse_mode**(	Optional ) - parse mode in HTML (optional)
  <details>
  <summary> example </summary>
    
```python 
#without parse_mode
send_message(bot=bot,chat_id=chat_id,text=f'hello :)')
#with parse_mode
send_message(bot=bot,chat_id=chat_id,text=f'<b>hello :)<b>',parse_mode='HTML') #make text bold
  ```
    
   </details>
    <br>
    <br>
    
 **reply_message**
  
```python 
def reply_message(bot,chat_id,msg_id,text,parse_mode):
  ```
  -**bot** - keyword where you store the token<br>
  -**chat_id** - you can use your chat id or use the chat_id method<br>
  -**text** - your message text<br>
  -**msg_id** - you can use your message id or use the message_id method <br>
  -**parse_mode**(	Optional ) - parse mode in HTML (optional)
  <details>
  <summary> example </summary>
    
```python 
#without parse_mode
reply_message(bot,msg_id=message_id,chat_id=chat_id,text="reply message ._.")
#with parse_mode
reply_message(bot,msg_id=message_id,chat_id=chat_id,text="<b>reply message is bold .-.</b>",parse_mode="HTML")#make text bold
  ```
    
   </details>
    <br>
    <br>

**send_sticker**
```python 
def send_sticker(bot,chat_id,sticker):
  ```
  -**bot** - keyword where you store the token<br>
  -**chat_id** - you can use your chat id or use the chat_id method<br>
  -**sticker** -unique sticker key, you can get it from [idstickerbot](https://t.me/idstickerbot)<br>

  <details>
  <summary> example </summary>
    
```python 
send_sticker(bot,chat_id=chat_id,sticker="CAACAgIAAxkBAAEGdwNjd-IwPaLBzeqJW1DJvDLGnYOJpwACQBMAAvZDSUjqTxpxhtdlhisE")
  ```
    
   </details>
   <br>
   <br>
   
**delete_message**
```python 
def delete_message(bot,chat_id,msg_id):
  ```
  -**bot** - keyword where you store the token<br>
  -**chat_id** - you can use your chat id or use the chat_id method<br>
  -**msg_id** - you can use your message id or use the message_id method <br>


  <details>
  <summary> example </summary>
    
```python 

delete_message(bot,msg_id=message_id,chat_id=chat_id) #this code will only work in a private chat, so that it would work for the bot to have the right to delete messages or replace message_id with reply_message_id, you can find an example in the folder example->delete_message.py

  ```
    
   </details>
