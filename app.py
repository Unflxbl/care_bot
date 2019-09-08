import json
from flask import Flask, request, make_response
from slackeventsapi import SlackEventAdapter
from care_bot import Bot
from slack import WebClient

app = Flask(__name__)
careBot = Bot()
slack_events_adapter = SlackEventAdapter(careBot.verification, "/slack/events", app)
# Указываем токен, его надо убрать в переменные окружения
client = WebClient("xoxb-714578520370-719690847425-8Q8msONK6u9M5SYJ7nq2xANg")

# Здесь сохраняем юзеров и их прогресс
users = {}


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
    # Здесь возникают ошибки, когда мы получаем ответ бота, потому что у него нет 'user' в event, но есть subtype
    # Надо придумать как обрабатывать эти ошибки
    if 'subtype' in event_data['event']:
        print('Bot replied you')
    if 'user' in event_data['event']:
        user_call = event_data['event']['user']
        if user_call in users:
            # print(users[user_call][-1])
            current_action = users[user_call][-1]
            # Здесь будет идти проверка последнего нажатого action баттона по айди, после чего мы отправляем это
            # сообщение повторно
            if current_action == 'a1':
                print("ок")
                client.chat_postMessage(channel="DMDTAU58X", blocks=[
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

        else:
            users[user_call] = ['a0']
            # print("Первое сообщение от бота")
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
    action_id = form_json['actions'][0]['action_id']
    timestamp = form_json['message']['ts']
    user_action = form_json['user']['id']
    print(timestamp)
    print(user_action)
    if action_id == 'a1':
        # Здесь мы проверяем айди кнопки, после ее нажатия мы добавляем ее в список значения для ключа этого юзера,
        # после чего мы вызываем обновление сообщения до следующего во флоу
        users[user_action].append(action_id)
        client.chat_update(
            ts=timestamp,
            channel="DMDTAU58X",
            blocks=[
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
    if action_id == 'a2':
        users[user_action].append(action_id)
        client.chat_update(ts=timestamp, channel="DMDTAU58X", blocks=[
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Про рабочий день, болезни, отпуск*\n *Регламенты работы*\n "
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://cdn.fishki.net/upload/post/2018/07/15/2651316/3-3.jpg",
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
                    "text": ":red_circle: Рабочий день и обед \n https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe98600428635ba8b27025 "
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":red_circle: График работы в отделе \n https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe98e10428635ba8b2702b/"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":red_circle: Отпуск \n https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe983f2c7d3a2f9011a0e0/"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":red_circle: Больничный\n https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe98b50428635ba8b27028/ "
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":red_circle: Регламенты по дисциплине \n https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe9a4d2c7d3a2f9011a0f7/ "
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":red_circle: Памятка по приходу/уходу из офиса \n https://docs.google.com/document/d/1sa7LtuTWPPX8bx47LPaNoNLQmoAcVcPZrffda19NbTY/edit "
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Если у тебя есть вопросы, пиши в Слаке в чатик для новых сотрудников.\n Чатик называется  #новенькие_забота "
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Дальше"
                    },
                    "value": "click_me_123",
                    "action_id": "a3"
                }
            }
        ])
    print(users)
    return users


if __name__ == '__main__':
    app.run(debug=True)
