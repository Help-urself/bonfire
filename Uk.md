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
- встановлюємо [ngrok](https://ngrok.com/) та запускаємо сервер по інструкції на сайті .
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
  -**parse_mode**(Не обов'язково) - parse mode для HTML
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
  -**bot** - Функція де в вас знаходиться TOKEN<br>
  -**chat_id** - Ви можете використовувати метод chat_id або своє айді чату<br>
  -**text** - Ваш Текст для повідомлення<br>
  -**parse_mode**(Не обов'язково) - parse mode для HTML<br>
  -**msg_id** - Ви можете використовувати метод message_id Або свое айді повідомлення<br>  
  <details>
  <summary> Приклад </summary>
    
```python 
#без parse_mode
reply_message(bot,msg_id=message_id,chat_id=chat_id,text="відповідь ._.")
#з parse_mode
reply_message(bot,msg_id=message_id,chat_id=chat_id,text="<b>відповідь жирним шрифтом .-.</b>",parse_mode="HTML")#робимо текст жирним шрифтом 
  ```
    
   </details>
    <br>
    <br>

**send_sticker**
```python 
def send_sticker(bot,chat_id,sticker):
  ```
   -**bot** - Функція де в вас знаходиться TOKEN<br>
  -**chat_id** - Ви можете використовувати метод chat_id або своє айді чату<br>
  -**sticker** - унікальний токен стікеру,ви можете його взяти у [idstickerbot](https://t.me/idstickerbot)<br>

  <details>
  <summary> Приклад </summary>
    
```python 
send_sticker(bot,chat_id=chat_id,sticker="CAACAgIAAxkBAAEGdwNjd-IwPaLBzeqJW1DJvDLGnYOJpwACQBMAAvZDSUjqTxpxhtdlhisE")#стікер з котиком :)
  ```
    
   </details>
   <br>
   <br>
   
**delete_message**
```python 
def delete_message(bot,chat_id,msg_id):
  ```
  -**bot** - Функція де в вас знаходиться TOKEN<br>
  -**chat_id** - Ви можете використовувати метод chat_id або своє айді чату<br
  -**msg_id** - Ви можете використовувати метод message_id (але тоді повідомлення користувача буде видалятися або у лічних повідомленнях,або у групах де у бота є на то права) чи встановити свое айді Повідомлення <br>


  <details>
  <summary> Приклад </summary>
    
```python 

delete_message(bot,msg_id=message_id,chat_id=chat_id) 

  ```
    
   </details>
    
    
  
    
    
  
  
  



