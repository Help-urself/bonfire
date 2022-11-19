# bonfire




**bonfire** — це framework [Telegram Bot API](https://core.telegram.org/bots/api) зроблений на [flask](https://flask.palletsprojects.com/en/2.2.x/ ) and [requests](https://requests.readthedocs.io/en/latest/) <br>
**Встановка**
```python 
git clone https://github.com/Help-urself/bonfire
```


## Приклади
<details>
  <summary> Нажміть </summary>


**Встанока веб-перехвадчика**
- встановлюємо [ngrok](https://ngrok.com/) and start the server according to the instructions on the website.
- та налаштовуємо webhook `https://api.telegram.org/botTOKEN/setWebhook?url=you url ngrok/hosting url`

### легкий [`send_message`](https://core.telegram.org/method/messages.sendMessage) запрос

```python
import os
import sys
sys.path.append(os.path.abspath('ваш путь к папці bonfire'))
import Bot
from Bot import Bots,edit_message,commands,run
from flask import Flask
from method import *
import time
from flask import request,Response
import requests
app = Flask(__name__)
bot=Bots("TOKEN")#налаштовуемо токен

@commands(app)#ця функція може бути лиш одна
def main():#назва функції не відіграє ролі,вона може бути люба 
 try:
    message=request.get_json()#отримуемо повідомлення
    chat_id,text,message_id,message_author_username,message_author_id,message_author_is_bot,message_author_first_name,message_author_language_code,message_date=parse_message(message=message)#важлива складова,не міняйте цей порядок,інакше код не буде працювати 
    if text == "/start": #ловимо комманду /start
        send_message(bot=bot,chat_id=chat_id,text=f'hello @{message_author_username}!')#відправляемо повідомлення 
 except Exception as error:
     print(error)
 return Response('OK', status=200)#повертаемо статус Post - (POST/ 200 OK)

if __name__ == '__main__':
       run(app)#app.run(port=8080,host="0.0.0.0",debug=True)
```
  </details>
  
## документація (в розробці)
<details>
  <summary> Нажміть </summary>
  
  
### Функції 

**send_message**
  
```python 
def send_message(bot,chat_id,text):
  ```
  -**bot** - Функція де в вас знаходиться TOKEN<br>
  -**chat_id** - Ви можете використовувати метод chat_id або своє айді<br>
  -**text** - Ваш Текст для повідомлення<br>
  -**parse_mode**(	Optional ) - parse mode для HTML (не обов'язково)
  <details>
  <summary> Приклад </summary>
    
```python 
#без parse_mode
send_message(bot=bot,chat_id=chat_id,text=f'Привіт Друже! :)')
#з parse_mode
send_message(bot=bot,chat_id=chat_id,text=f'<b>Привіт друже :)<b>',parse_mode='HTML') #виділить текст жирним курсивом 
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
    
    
  
    
    
  
  
  



