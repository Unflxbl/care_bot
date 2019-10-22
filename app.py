import json
from flask import Flask, request, make_response
from slackeventsapi import SlackEventAdapter
from care_bot import Bot
from slack.web.client import WebClient
from messages import blocks, block_greeting
from messages_mvp import messages

app = Flask(__name__)
careBot = Bot()
slack_events_adapter = SlackEventAdapter(careBot.verification, "/slack/events", app)
# Указываем токен, его надо убрать в переменные окружения
client = WebClient("xoxb-714578520370-719690847425-tyAApHxaq7Fte00SygTwQ07K")

# Здесь сохраняем юзеров и их прогресс
users = {}

# Указываем айди нашего бота, в него будем постить сообщения
bot_channel = 'DMDTAU58X'


# Верификация URL для Events
@app.route("/slack/events", methods=["GET", "POST"])
def hears():
    response = json.loads(request.data)
    if "challenge" in response:
        return make_response(response["challenge"], 200, {"content_type": "application/json"})


# Обработчик сообщений боту. Суть этой функции в том, что пользователь пишет боту любой текст, бот приветствует
# пользователя и предлагает ему либо продолжить обучение на том месте, где он остановился (не обновляя последнее окно
# с сообщением от бота, а просто показывая его вновь. Если пишет пользователь впервые, то ему показывается первое
# сообщение от бота, после чего пользователь жмет кнопки (его прогресс сохраняется через id кнопок) и двигается дальше
# по флоу.
@slack_events_adapter.on("message")
def handle_message(event_data):
    # print(event_data)
    # Здесь проверем тип сообщения, которе было написано в боте (это либо бот отвечает, либо пишет юзер)
    if 'subtype' in event_data['event']:
        print('Bot replied you')
    if 'user' in event_data['event']:
        user_call = event_data['event']['user']
        if user_call in users:
            client.chat_postMessage(channel=bot_channel,
                                    text="Прости, я пока что не настолько умен чтобы понять тебя :( \n Но сейчас ты можешь перейти к плану обучения")
            # Здесь необходимо показывать лобби с текущим прогрессом
        else:
            users[user_call] = ['a0']
            # Первое сообщение юзера от бота, начинается трекаться прогресс
            client.chat_postMessage(channel=bot_channel, text="И тебе привет!", blocks=block_greeting())
        return users


# Обработчик action кнопок
@app.route("/slack/buttons", methods=["POST", "GET"])
def message_actions():
    form_json = json.loads(request.form["payload"])
    print(form_json)
    # Получаем айди экшн батона из пришедшего запроса.
    action_id = form_json['actions'][0]['action_id']
    timestamp = form_json['message']['ts']
    user_action = form_json['user']['id']
    print(timestamp)
    print(user_action)

    # Первый блок - меню
    if action_id == 'start':
        # Здесь мы проверяем айди кнопки, после ее нажатия мы добавляем ее в список значения для ключа этого юзера,
        # после чего мы вызываем обновление сообщения до следующего во флоу
        if action_id not in users[user_action]:
            users[user_action].append(action_id)
        # Проверка импорта функции, возврающей значение для отправки мессаджей
        client.chat_update(ts=timestamp, channel=bot_channel, blocks=blocks(action_id))
    if action_id == 'a1':
        if action_id not in users[user_action]:
            users[user_action].append(action_id)
            print(blocks(action_id))
        client.chat_update(ts=timestamp, channel=bot_channel, blocks=messages(action_id))
    if action_id == 'a2':
        if action_id not in users[user_action]:
            users[user_action].append(action_id)
            print(blocks(action_id))
        client.chat_update(ts=timestamp, channel=bot_channel, blocks=messages(action_id))
    if action_id == 'a3':
        if action_id not in users[user_action]:
            users[user_action].append(action_id)
        client.chat_update(ts=timestamp, channel=bot_channel, blocks=messages(action_id))
    if action_id == 'a4':
        if action_id not in users[user_action]:
            users[user_action].append(action_id)
        client.chat_update(ts=timestamp, channel=bot_channel, blocks=messages(action_id))
    if action_id == 'a5':
        if action_id not in users[user_action]:
            users[user_action].append(action_id)
        client.chat_update(ts=timestamp, channel=bot_channel, blocks=messages(action_id))
    if action_id == 'a6':
        if action_id not in users[user_action]:
            users[user_action].append(action_id)
        client.chat_update(ts=timestamp, channel=bot_channel, blocks=messages(action_id))
    if action_id == 'a7':
        if action_id not in users[user_action]:
            users[user_action].append(action_id)
        client.chat_update(ts=timestamp, channel=bot_channel, blocks=messages(action_id))
    if action_id == 'a8':
        if action_id not in users[user_action]:
            users[user_action].append(action_id)
        client.chat_update(ts=timestamp, channel=bot_channel, blocks=messages(action_id))
    if action_id == 'a9':
        if action_id not in users[user_action]:
            users[user_action].append(action_id)
        client.chat_update(ts=timestamp, channel=bot_channel, blocks=messages(action_id))
    if action_id == 'a10':
        if action_id not in users[user_action]:
            users[user_action].append(action_id)
        client.chat_update(ts=timestamp, channel=bot_channel, blocks=messages(action_id))
    if action_id == 'a11':
        if action_id not in users[user_action]:
            users[user_action].append(action_id)
        client.chat_update(ts=timestamp, channel=bot_channel, blocks=messages(action_id))
    if action_id == 'a12':
        if action_id not in users[user_action]:
            users[user_action].append(action_id)
        client.chat_update(ts=timestamp, channel=bot_channel, blocks=messages(action_id))
    if action_id == 'a13':
        if action_id not in users[user_action]:
            users[user_action].append(action_id)
        client.chat_update(ts=timestamp, channel=bot_channel, blocks=messages(action_id))
    if action_id == 'a14':
        if action_id not in users[user_action]:
            users[user_action].append(action_id)
        client.chat_update(ts=timestamp, channel=bot_channel, blocks=messages(action_id))
    if action_id == 'a15':
        if action_id not in users[user_action]:
            users[user_action].append(action_id)
        client.chat_update(ts=timestamp, channel=bot_channel, blocks=messages(action_id))
    if action_id == 'back':
        if action_id not in users[user_action]:
            users[user_action].append(action_id)
        client.chat_update(ts=timestamp, channel=bot_channel, blocks=blocks('start'))
    print(users)
    return users


if __name__ == '__main__':
    app.run(debug=True)
