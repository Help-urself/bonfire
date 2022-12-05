# bonfire




bonfire this framework for [Telegram Bot API](https://core.telegram.org/bots/api) built on [flask](https://flask.palletsprojects.com/en/2.2.x/ ) and [requests](https://requests.readthedocs.io/en/latest/) <br>
**Ukrainian launge translate -> [click](https://github.com/Help-urself/bonfire/blob/main/Uk.md)**<br>
**instaling**
```python 
git clone https://github.com/Help-urself/bonfire
```
or

```python 
pip install -i https://test.pypi.org/simple/ bonfire-tgb
pip install bonfire-tg-libraly


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

import requests
from flask import Flask
import os
import sys
sys.path.append(os.path.abspath('you path to bonfire'))
from bonfiree.methods import *
from bonfiree.Bot import *


app = Flask(__name__)
token = "..."#token


@bot.handler
def start():  
    if msg.text == "/start": 
     send_message(token,chat_id=msg.chat_id,text=f"Hello {msg.author_username},is test bot")#send message

@commands(app)
def main():
 global msg
 msg=message(request.get_json())#message handler
 start()#start function start


 return Response('OK', status=200)#return status ok to cmd
if __name__ == '__main__':
       run(app)

       """set-webhook - > https://api.telegram.org/botTOKEN/setWebhook?url=URL"""

```

```py
#pip install

import requests
from flask import Flask
from bonfiree.methods import *
from bonfiree.Bot import *


app = Flask(__name__)
token = "..."#token


@bot.handler
def start():  
    if msg.text == "/start": 
     send_message(token,chat_id=msg.chat_id,text=f"Hello {msg.author_username},is test bot")#send message

@commands(app)
def main():
 global msg
 msg=message(request.get_json())#message handler
 start()#start function start


 return Response('OK', status=200)#return status ok to cmd
if __name__ == '__main__':
       run(app)

       """set-webhook - > https://api.telegram.org/botTOKEN/setWebhook?url=URL"""
```

  </details>
  
## Documentation (in development)
<details>
  <summary> Click </summary>
  
  
### functions

**send_message**
  
```python 
def send_message(token,chat_id,text):
  ```
  -**token** - keyword where you store the token<br>
  -**chat_id** - you can use your chat id or use the msg.chat_id method<br>
  -**text** - 
your message text<br>
  -**parse_mode**(	Optional ) - parse mode in HTML (optional)
  <details>
  <summary> example </summary>
    
```python 
msg=message(request.get_json())

#without parse_mode
send_message(token=bot,chat_id=msg.chat_id,text=f'hello :)')
#with parse_mode
send_message(token=bot,chat_id=msg.chat_id,text=f'<b>hello :)<b>',parse_mode='HTML') #make text bold
  ```
    
   </details>
    <br>
    <br>
    
 **reply_message**
  
```python 
def reply_message(token,chat_id,msg_id,text,parse_mode):
  ```
  -**token** - keyword where you store the token<br>
  -**chat_id** - you can use your chat id or use the msg.chat_id method<br>
  -**text** - your message text<br>
  -**msg_id** - you can use your message id or use the msg.id method <br>
  -**parse_mode**(	Optional ) - parse mode in HTML (optional)
  <details>
  <summary> example </summary>
    
```python 
 msg=message(request.get_json())
#without parse_mode
reply_message(token,msg_id=msg.id,chat_id=msg.chat_id,text="reply message ._.")
#with parse_mode
reply_message(token,msg_id=msg.id,chat_id=msg.chat_id,text="<b>reply message is bold .-.</b>",parse_mode="HTML")#make text bold
  ```
    
   </details>
    <br>
    <br>

**send_sticker**
```python 
def send_sticker(token,chat_id,sticker):
  ```
  -**token** - keyword where you store the token<br>
  -**chat_id** - you can use your chat id or use the msg.chat_id method<br>
  -**sticker** -unique sticker key, you can get it from [idstickerbot](https://t.me/idstickerbot)<br>

  <details>
  <summary> example </summary>
    
```python 
send_sticker(token,chat_id=msg.chat_id,sticker="CAACAgIAAxkBAAEGdwNjd-IwPaLBzeqJW1DJvDLGnYOJpwACQBMAAvZDSUjqTxpxhtdlhisE")
  ```
    
   </details>
   <br>
   <br>
   
**delete_message**
```python 
def delete_message(token,chat_id,msg_id):
  ```
  -**token** - keyword where you store the token<br>
  -**chat_id** - you can use your chat id or use the msg.chat_id method<br>
  -**msg_id** - you can use your message id or use the msg.id method <br>


  <details>
  <summary> example </summary>
    
```python 

delete_message(token,msg_id=msg.id,chat_id=msg.chat_id) #this code will only work in a private chat, so that it would work for the bot to have the right to delete messages or replace message_id with reply_message_id, you can find an example in the folder example->delete_message.py

  ```
    
   </details>