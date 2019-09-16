def block_greeting():
    blocks_a0 = [
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
    ]
    return blocks_a0


def blocks(action_id):
    if action_id == 'a1':
        block = [
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
                    "text": "Для начала работы зайди на Gmail в https://mail.google.com c твоей новой рабочей почтой xxxxxxxx@elama.ru "
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Зарегистрируйся на elama.ru с новой рабочей почтой xxxxxxxx@elama.ru"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Проверь, что тебе пришло приглашение в Gmail для доступа в почтовый сервис Helpscout"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Зайди в Корпортал http://corportal.trinet.ru под доступами с листа у компьютера портал, в котором нужно отмечать рабочее время "
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Ознакомился? Идем дальше! "
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
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Перейти к плану обучения"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Перейти"
                    },
                    "value": "click_me_123",
                    "action_id": "s2"
                }
            }
        ]
    if action_id == 'a2':
        block = [
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
                    "text": "Рабочий день и обед \n https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe98600428635ba8b27025 "
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "График работы в отделе \n https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe98e10428635ba8b2702b/"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Отпуск \n https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe983f2c7d3a2f9011a0e0/"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Больничный\n https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe98b50428635ba8b27028/ "
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Регламенты по дисциплине \n https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe9a4d2c7d3a2f9011a0f7/ "
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Памятка по приходу/уходу из офиса \n https://docs.google.com/document/d/1sa7LtuTWPPX8bx47LPaNoNLQmoAcVcPZrffda19NbTY/edit "
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
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Перейти к плану обучения "
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Перейти",
                    },
                    "value": "click_me_123",
                    "action_id": "lobby"
                }
            }
        ]
    if action_id == 'a3':
        block = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Что такое еЛама* "
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://trinixy.ru/pics5/20160411/alpaca_01.jpg",
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
                    "text": "Презентация \n https://docs.google.com/a/elama.ru/presentation/d/1AfvUvt2uKLA_m407vISm7WwPzhA9VyB-KGfjSTo4p-A/edit?usp=sharing "
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Статья \n http://help.elama.ru/hc/ru/articles/208045535"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Преимущства \n https://pl.elama.ru/advantages"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Пора двигаться дальше! "
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Дальше"
                    },
                    "value": "click_me_123",
                    "action_id": "a4"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Перейти к плану обучения "
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Перейти",
                    },
                    "value": "click_me_123",
                    "action_id": "lobby"
                }
            }
        ]
    if action_id == 'a4':
        block = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Кто и чем занимается в Службе Заботы* "
                },
                "accessory": {
                    "type": "image",
                    "image_url": "http://zhivotnue.ru/image/domashnie_zhivotnue/selskoxoz_zhivotnue/alpaka/1.jpg",
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
                    "text": "Служба Заботы: Кто? Что? Зачем?  \n https://drive.google.com/open?id=1bYKuWwbRDVFDTzmtSh5QO60urmaedtCfS97YHJhVez0"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Служба Заботы: Ху из Ху \n https://docs.google.com/presentation/d/1i8A4gF4penHI8IVBmC4CNIsJ5zRHedsFqKvXxiJBTXQ/edit#slide=id.g5a8b5a54b5_11_803"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Структура отдела \n https://miro.com/app/board/o9J_kxhclu8=/"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Пора двигаться дальше! "
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
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Перейти к плану обучения "
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Перейти",
                    },
                    "value": "click_me_123",
                    "action_id": "lobby"
                }
            }
        ]

    if action_id == 'lobby':
        block = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*План обучения Службы Заботы* "
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsFnLIgHtbfIoBt5jTwpZLPmvWgBEXKLAuqZlrunstZHqjoijL",
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
                    "text": "Раздел 1: Знакомство "
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Перейти"
                    },
                    "value": "click_me_123",
                    "action_id": "s2"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Вернуться к обучению? "
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Да!"
                    },
                    "value": "click_me_123",
                    "action_id": "a4"
                }
            }
        ]
    if action_id == 's2':
        block = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Раздел 1: Знакомство* "
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsFnLIgHtbfIoBt5jTwpZLPmvWgBEXKLAuqZlrunstZHqjoijL",
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
                    "text": "Знакомство с офисом и коллегами.Корпортал, Helpscout, Slack, Gmail. Помощь еЛамы для Заботы в Helpscout Docs "
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Перейти"
                    },
                    "value": "click_me_123",
                    "action_id": "s3"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Про рабочий день, болезни, отпуск, регламенты работыs "
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Перейти"
                    },
                    "value": "click_me_123",
                    "action_id": "s1"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Что такое еЛама"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Перейти"
                    },
                    "value": "click_me_123",
                    "action_id": "s1"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Кто и чем занимается в Службе Заботы еЛама"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Перейти"
                    },
                    "value": "click_me_123",
                    "action_id": "s1"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Пора двигаться дальше! "
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Дальше"
                    },
                    "value": "click_me_123",
                    "action_id": "a4"
                }
            }
        ]
    if action_id == 's3':
        block = [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Раздел 1: Знакомство* "
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsFnLIgHtbfIoBt5jTwpZLPmvWgBEXKLAuqZlrunstZHqjoijL",
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
                    "text": "Знакомство с офисом и коллегами.Корпортал, Helpscout, Slack, Gmail. Помощь еЛамы для Заботы в Helpscout Docs "
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Перейти"
                    },
                    "value": "click_me_123",
                    "action_id": "s2"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Для начала работы зайди на Gmail в https://mail.google.com c твоей новой рабочей почтой xxxxxxxx@elama.ru "
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Зарегистрируйся на elama.ru с новой рабочей почтой xxxxxxxx@elama.ru"
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
                    "text": "Зайди в Корпортал http://corportal.trinet.ru под доступами с листа у компьютера - портал, в котором нужно отмечать рабочее время "
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Про рабочий день, болезни, отпуск, регламенты работыs "
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Перейти"
                    },
                    "value": "click_me_123",
                    "action_id": "s1"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Что такое еЛама"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Перейти"
                    },
                    "value": "click_me_123",
                    "action_id": "s1"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Кто и чем занимается в Службе Заботы еЛама"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Перейти"
                    },
                    "value": "click_me_123",
                    "action_id": "s1"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Пора двигаться дальше! "
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Дальше"
                    },
                    "value": "click_me_123",
                    "action_id": "a4"
                }
            }
        ]
    return block
