# bonfire




**bonfire** — framework for [Telegram Bot API](https://core.telegram.org/bots/api) built on [flask](https://flask.palletsprojects.com/en/2.2.x/ ) and [requests](https://requests.readthedocs.io/en/latest/)


## Examples
<details>
  <summary> Click </summary>


**1.install interceptor**
- install [ngrok](https://ngrok.com/) and start the server according to the instructions on the website.
- set webhook `https://api.telegram.org/botTOKEN/setWebhook?url=you url ngrok/hosting url`

### Simple [`send_message`](https://core.telegram.org/method/messages.sendMessage) request

```python
import os
import sys
sys.path.append(os.path.abspath('your campfire folder path'))
import Bot
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
    if reply_message_text == "/start": #/start command handler
        send_message(bot=bot,chat_id=chat_id,text=f'hello @{message_author_username}!')#send message
 except Exception as error:
     print(error)
 return Response('OK', status=200)#return to cmd (POST/ 200 OK)

if __name__ == '__main__':
       run(app)#app.run(port=8080,host="0.0.0.0",debug=True)
```
  
## documentation (in development)
<details>
  <summary> Click </summary>


**1.fuction**
- send_message
  
- set webhook `https://api.telegram.org/botTOKEN/setWebhook?url=you url ngrok/hosting url`

### Simple [`send_message`](https://core.telegram.org/method/messages.sendMessage) request

```python
import os
import sys
sys.path.append(os.path.abspath('your campfire folder path'))
import Bot
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
    if reply_message_text == "/start": #/start command handler
        send_message(bot=bot,chat_id=chat_id,text=f'hello @{message_author_username}!')#send message
 except Exception as error:
     print(error)
 return Response('OK', status=200)#return to cmd (POST/ 200 OK)

if __name__ == '__main__':
       run(app)#app.run(port=8080,host="0.0.0.0",debug=True)
```


