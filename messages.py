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
                "action_id": "start"
            }
        }
    ]
    return blocks_a0


def blocks(action_id):
    if action_id == 'start':
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
				"action_id": "a1"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Раздел 2: Инструменты eLama и основы интернет рекламы "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
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
				"text": "Раздел 3: Изучаем Яндекс.Директ "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a3"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Раздел 4: Выходим на почту. HelpScout "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a4"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Раздел 5: Изучаем подробнее аукцион, ценообразование в Директе и два основных инструмента eLama "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a5"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Раздел 6: Изучаем Google Рекламу "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a6"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Раздел 7: Выходим в чат Carrot Quest "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a7"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Раздел 8: Изучаем Таргетированную рекламу. Facebook, Вконтакте, MyTarget "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a8"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Раздел 9: Изучаем систему аналитики Я.Метрику и Ретаргетинг "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a9"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Раздел 10: Выходим на телефон Mango Office "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a10"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Раздел 11: Изучаем системы Коллтрекинга "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a11"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Раздел 12: Изучаем дополнительную информацию по Яндексу "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a12"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Раздел 13: Изучаем систему аналитики Google Analytics и Ремаркетинг "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a13"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Раздел 14: Экзамен "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a14"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Раздел 15: Что дальше? "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a15"
			}
		},
		{
			"type": "divider"
		}
	]
    if action_id == 'a1':
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
				"text": "Знакомство с офисом и коллегами. Корпортал, Helpscout, Slack, Gmail. Помощь еЛамы для Заботы в Helpscout Docs"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a1_1"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Про рабочий день, болезни, отпуск, регламенты работы"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a1_2"
			}
		},
		{
			"type": "divider"
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
				"action_id": "a1_3"
			}
		},
		{
			"type": "divider"
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
				"action_id": "a1_3"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Сделать небольшую презентацию о себе"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a1_4"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Библиотека знаний"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a1_5"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"style": "danger",
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Назад"
					},
					"value": "click_me_123",
					"action_id": "back"
				}
			]
		},
		{
			"type": "divider"
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
				"text": "*Раздел 2: Инструменты eLama и основы интернет рекламы* "
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
				"text": "Контекстная реклама: Основы"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a2_1"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Таргетированная реклама в соцсетях: Основы"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a2_2"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Интерфейс и инструменты еЛамы"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a2_3"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Акции для новых клиентов в еЛаме "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a2_4"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Тест по услугам еЛама"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a2_5"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Доступы к рекламным кабинетам в еЛама"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a2_6"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Тарифы в еЛама"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a2_7"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Партнерская программа в еЛаме "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a2_8"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"style": "danger",
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Назад"
					},
					"value": "click_me_123",
					"action_id": "start"
				}
			]
		},
		{
			"type": "divider"
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
				"text": "*Изучаем Яндекс.Директ* "
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
				"text": "Обзор рекламы в Директе "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "start"
				},
				"value": "click_me_123",
				"action_id": "a3_1"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Поисковые кампании"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a3_2"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Символы и операторы. Сервис подбора слов Wordstat. Минус-слова"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a3_3"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "РСЯ кампании"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a3_4"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Исключение пересекающихся ключевых запросов - \"Кроссминусация\" в еЛаме"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a3_5"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Модерация в Директе. Правила и требования к рекламе"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a3_6"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Что еще нужно знать"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a3_7"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Коммуникация с менеджером Яндекс Директа "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a3_8"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Тест"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a3_9"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"style": "danger",
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Назад"
					},
					"value": "click_me_123",
					"action_id": "start"
				}
			]
		},
		{
			"type": "divider"
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
				"text": "*Выходим на почту Helpscout* "
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
				"text": "KeePass "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a4_1"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Как писать письма. Где искать инфу в почте (тема, приветствие, шаблоны ответов).\n Регламенты ответа. Заметки в Helpscout. Телефоны Яндекса, гугла, бухгалтерии. Пароли. Теги к письмам. \nКак писать в Яндекс по вопросам модерации и не только. \nПростая коммуникация с менеджером Яндекса по баллам, представителям, копированию c CTR "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a4_2"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Простые письма и задачи: приглашения, копирование, модерация еЛамы, переводы ручные, автоматические письма от яндекса, клиент потерял пароль, простые письма клиентов "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a4_3"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Технические ошибки и баги. Инциденты "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a4_4"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"style": "danger",
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Назад"
					},
					"value": "click_me_123",
					"action_id": "start"
				}
			]
		},
		{
			"type": "divider"
		}
	]
    if action_id == 'a5':
        block = [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Изучаем подробнее аукцион, ценообразование в Директе и два основных инструмента еЛама* "
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
				"text": "Аукцион и Ценообразование в Директ "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a5_1"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Стратегии размещения в Директе "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a5_2"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Автоматическое управление ставками еЛама или Бид-менеджер или Бидер\nДоп.настройка \"Сео-бидер\" для управления ставками "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a5_3"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "UTM-разметка"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a5_4"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Практика: Создать рекламные кампании в Директе"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a5_5"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Тест 2 "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a5_6"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"style": "danger",
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Назад"
					},
					"value": "click_me_123",
					"action_id": "start"
				}
			]
		},
		{
			"type": "divider"
		}
	]
    if action_id == 'a6':
        block = [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Изучаем Google Рекламу* "
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
				"text": "Обзор рекламы Google Ads"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a6_1"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Типы соответствия. Планировщик ключевых слов. Минус-слова "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a6_2"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Правила показа"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a6_3"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Ценообразование в Google Ads. Ставки, Рейтинг, и Аукцион на Поиске и КМС "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a6_4"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Поисковые кампании"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a6_5"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "КМС кампании"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a6_6"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Модерация в  Google Ads. Правила и требования"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a6_7"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Адреса в объявлениях в Google Ads "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a6_8"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Google Merchant"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a6_9"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Практика: Создать рекламные кампании в Google Ads"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a6_10"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"style": "danger",
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Назад"
					},
					"value": "click_me_123",
					"action_id": "start"
				}
			]
		},
		{
			"type": "divider"
		}
	]
    if action_id == 'a7':
        block = [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Выходим в чат Carrot Quest* "
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
				"text": "Подключение к чату на сайте. Общение с клиентами в чате   "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a7_1"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Тест 3"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a7_2"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"style": "danger",
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Назад"
					},
					"value": "click_me_123",
					"action_id": "start"
				}
			]
		},
		{
			"type": "divider"
		}
	]
    if action_id == 'a8':
        block = [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Изучаем таргетированную рекламу: Facebook, Вконтакте, MyTarget* "
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
				"text": "Вконтакте "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a8_1"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Facebook Часть 1 "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a8_2"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Facebook Часть 2 "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a8_3"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Facebook Часть 3 "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a8_4"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "MyTarget"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a8_5"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"style": "danger",
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Назад"
					},
					"value": "click_me_123",
					"action_id": "start"
				}
			]
		},
		{
			"type": "divider"
		}
	]
    if action_id == 'a9':
            block = [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Изучаем систему аналитики Я.Метрику и Ретаргетинг* "
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
				"text": "Основы работы с Яндекс.Метрикой"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a9_1"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Я.Метрика. Счетчик Я.Метрики"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a9_2"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Сегменты Метрики "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a9_3"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Цели Метрики"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a9_4"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Отчеты Метрики"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a9_5"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Особенности статистики в Директе и в Метрике "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a9_6"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Вебвизор"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a9_7"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Скликивание, высокий процент показов"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a9_8"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Ретаргетинг  и Подбор аудитории в Директе "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a9_9"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Я.Аудитории"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a9_10"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Тест 4"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a9_11"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"style": "danger",
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Назад"
					},
					"value": "click_me_123",
					"action_id": "start"
				}
			]
		},
		{
			"type": "divider"
		}
	]
    if action_id == 'a10':
            block = [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Выходим на телефон Mango Office* "
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
				"text": "Подготовка к телефону"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a10_1"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Подготовка"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a10_2"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Коммуникация по телефону с разными типами клиентов. Как приветствовать. Как ставить на удержание. Как переключать на другого сотрудника"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a10_3"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Разговоры. Записи разговоров "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a10_4"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"style": "danger",
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Назад"
					},
					"value": "click_me_123",
					"action_id": "start"
				}
			]
		},
		{
			"type": "divider"
		}
	]
    if action_id == 'a11':
            block = [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Изучаем системы Коллтрекинга* "
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
				"text": "Системы Коллтрекинга "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a11_1"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"style": "danger",
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Назад"
					},
					"value": "click_me_123",
					"action_id": "start"
				}
			]
		},
		{
			"type": "divider"
		}
	]
    if action_id == 'a12':
            block = [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Изучаем дополнительную информацию по Яндексу* "
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
				"text": "Имиджевая реклама: стимулирование спроса "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a12_1"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Performance-реклама: от спроса к продажам"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a12_2"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Персонализированная реклама: возврат клиентов и доппродажи"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a12_3"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Я.Справочник"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a12_4"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"style": "danger",
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Назад"
					},
					"value": "click_me_123",
					"action_id": "start"
				}
			]
		},
		{
			"type": "divider"
		}
	]
    if action_id == 'a13':
            block = [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Изучаем систему аналитики Google Analytics и Ремаркетинг* "
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
				"text": "Google Analytics "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a13_1"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Выгрузка данных о расходах из Директа в Analytics через еЛама "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a13_2"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Ремаркетинг в Google AdWords"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a13_3"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"style": "danger",
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Назад"
					},
					"value": "click_me_123",
					"action_id": "start"
				}
			]
		},
		{
			"type": "divider"
		}
	]
    if action_id == 'a14':
            block = [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Экзамен* "
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
				"text": "Вопросы к экзамену "
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Перейти"
				},
				"value": "click_me_123",
				"action_id": "a14_1"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"style": "danger",
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Назад"
					},
					"value": "click_me_123",
					"action_id": "start"
				}
			]
		},
		{
			"type": "divider"
		}
	]
    if action_id == 'a15':
        	block = [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Что дальше?"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"style": "danger",
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Назад"
					},
					"value": "click_me_123",
					"action_id": "start"
				}
			]
		},
		{
			"type": "divider"
		}
	]

    return block
