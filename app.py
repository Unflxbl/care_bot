import json
from flask import Flask, request, make_response
from slackeventsapi import SlackEventAdapter
from care_bot import Bot
from slack import WebClient

app = Flask(__name__)
careBot = Bot()
slack_events_adapter = SlackEventAdapter(careBot.verification, "/slack/events", app)
# Указываем токен
client = WebClient("xoxb-714578520370-719690847425-FrrhGzlmUOyWrbE4ZHRKgHSr")

# Здесь сохраняем юзеров и их прогресс
users = {}

# Верификация URL для Events
@app.route("/slack/events", methods=["GET", "POST"])
def hears():
    response = json.loads(request.data)
    if "challenge" in response:
        return make_response(response["challenge"], 200, {"content_type": "application/json"})


# Используя SlackEvent мы определяем сообщение, которое пользователь пишет боту и предлагаем начать обучение
@slack_events_adapter.on("message")
def handle_message(event_data):
    if event_data["event"]["type"] == 'message' and event_data["event"]["channel"] == 'DMDTAU58X' and event_data["event"]["text"] == 'Привет!':#and not event_data["event"]["subtype"] == 'bot_message':
        # Записываем юзера, который обращается к боту впервые.
        # Здесь сделаем проверку на то, какой юзер обращается и на каком он этапе обучения
        # После этой проверки выдаем ему небольшой текст и предлагаем ему продолжить с того места где он остановился
        user_check = event_data["event"]["user"]
        print(user_check)
        users[user_check] = []
        #print(users)
        client.chat_postMessage(channel='DMDTAU58X', text="И тебе привет!", blocks=[
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Привет! Я Care Bot - бот для помощи тебе в прохождении плана обучения.\nТебе предстоит многое узнать, но не пугайся, все начинается с малого! \n Удачи!"
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEZbsTYd3dgUstbiho2zY1GI7yJoQ0XMGH7RjMFbJpUT6shh0G",
                    "alt_text": "palm tree"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Если ты готов начать учиться, нажми кнопку *Поехали!* и начинай двигаться по плану "
                            "обучения. "
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Поехали!",

                    },
                    "value": "click_me_123",
                    "action_id": "a1"
                }
            }
        ])
    return users

# Обработчик action кнопок
@app.route("/slack/buttons", methods=["POST", "GET"])
def message_actions():
    form_json = json.loads(request.form["payload"])
    print(form_json)
    # Получаем айди экшн батона из пришедшего запроса. Надо узнать другой способ получения айди или привести все
    # формы к одному виду
    action_id = form_json['message']['blocks'][3]['accessory']['action_id']
    if action_id == 'a1':
        users['UM0H0FB6E'].append(action_id)
        client.chat_postMessage(channel='DMDTAU58X', text="Идем дальше!", blocks=[
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Знакомство с офисом и коллегами*\n *Корпортал, Helpscout, Gmail*"
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://i.playground.ru/i/pix/351851/image.jpg",
                    "alt_text": "alpaca"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":red_circle: Для начала работы зайди на Gmail в https://mail.google.com c твоей новой рабочей "
                            "почтой xxxxxxxx@elama.ru "
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":red_circle: Зарегистрируйся на elama.ru с новой рабочей почтой xxxxxxxx@elama.ru"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":red_circle: Проверь, что тебе пришло приглашение в Gmail для доступа в почтовый сервис Helpscout"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":red_circle: Зайди в Корпортал http://corportal.trinet.ru под доступами с листа у компьютера -  "
                            "портал, в котором нужно отмечать рабочее время "
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Ознакомился? Идем дальше :smile: "
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Дальше"
                    },
                    "value": "click_me_123",
                    "action_id": "a2"
                }
            }
        ])
    print(users)
    return users

if __name__ == '__main__':
    app.run(debug=True)
