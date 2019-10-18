def messages(action_id):
 # Сменить экшн айди, здесь уже полные сообщения со всеми открытыми меню
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
				"text": "1. Для начала работы зайди на <https://mail.google.com|Gmail> c твоей новой рабочей почтой xxxxxxxx@elama.ru\n 2. Зарегистрируйся на <https://elama.ru|elama.ru> с новой рабочей почтой xxxxxxxx@elama.ru\n 3. Проверь, что тебе пришло приглашение в Gmail для доступа в почтовый сервис Helpscout\n 4. Зайди в корпоративный мессенджер <https://docs.google.com/document/d/1_tFJEEY8kKDr17-eLA6bj7hbwyZD38sYgP9P56BN--8/edit|Slack> \n 5. Зайди в <http://corportal.trinet.ru|Корпортал> под доступами с листа у компьютера -  портал, в котором нужно отмечать рабочее время"
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
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe98600428635ba8b27025/|Рабочий день и обед> \n <https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe98e10428635ba8b2702b/|График работы в отделе>\n<https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe983f2c7d3a2f9011a0e0/|Отпуск>\n<https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe98b50428635ba8b27028/|Больничный>\n<https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe9a4d2c7d3a2f9011a0f7/|Регламенты по дисциплине>\n<https://docs.google.com/document/d/1sa7LtuTWPPX8bx47LPaNoNLQmoAcVcPZrffda19NbTY/edit|Памятка по приходу/уходу из офиса>\nЕсли у тебя есть вопросы, пиши в Слаке в чатик для новых сотрудников. Чатик называется  #новенькие_забота"
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
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/a/elama.ru/presentation/d/1AfvUvt2uKLA_m407vISm7WwPzhA9VyB-KGfjSTo4p-A/edit?usp=sharing|Презентация>\n<http://help.elama.ru/hc/ru/articles/208045535|Статья>\n<https://pl.elama.ru/advantages|Преимущества>"
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
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://drive.google.com/open?id=1bYKuWwbRDVFDTzmtSh5QO60urmaedtCfS97YHJhVez0|Служба Заботы: Кто? Что? Зачем?>\n<https://docs.google.com/presentation/d/1i8A4gF4penHI8IVBmC4CNIsJ5zRHedsFqKvXxiJBTXQ/edit#slide=id.g5a8b5a54b5_11_803|Служба Заботы \"Ху из Ху\">\n<https://miro.com/app/board/o9J_kxhclu8=/|Структура отдела>"

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
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "У нас есть традиция: каждый новый сотрудник отдела заботы рассказывает о себе, своих увлечениях и жизни в презентации :) Как это сделать: \n1. Зайди в <https://drive.google.com|Google Drive>\n2. Создай презентацию о себе\n3. Открой доступ к презентации по ссылке\n4. Кинь ссылку с готовой презентацией в <https://secure.helpscout.net/conversation/272543529/1152773/?folderId=568624|эту> цепочку писем \n5. Напиши об этом в чат #bitches_managers"
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
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Здесь собран список ресурсов, к которым ты можешь обращаться в течение всего обучения и даже после :smile:\n Он пригодится тебе в будущем для быстрого поиска информации:\n1. <https://help.elama.global/hc/ru|Помощь еЛамы> \n2. <https://ppc.world/|Образовательный портал еЛамы> \n3. <https://elama.ru/blog/|Блог еЛамы> \n4. <https://www.youtube.com/channel/UCWFX2t6rtMyHvzB9eHNh_qg|Ютуб-канал еЛамы>\n 5. <https://yandex.ru/support/direct|Справка Яндекс.Директ>\n 6.<https://yandex.ru/support/metrika/|Справка Яндекс.Метрика>\n7. <https://yandex.ru/adv/|Блог Яндекса> \n8. <https://support.google.com/google-ads/?hl=ru#topic=74561579|Справка Google Ads>. \n9. <https://support.google.com/analytics/?hl=ru#topic=354490610|Cправка Google Analytics> \n10. <https://yagla.ru/blog/|Блог Яглы по контекстной рекламе> \n\nРазделы с инструкциями и статьями Docs в Helpscout можно найти <http://joxi.ru/V2VbpwJcdYEn32|тут> "
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
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://help.elama.global/hc/ru/articles/207432709|Знакомство с Яндекс.Директом>"
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
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://oneretarget.com/ru/wiki/таргетинг-в-соцсетях|Что такое таргетированная реклама>\n <https://vk.com/ads/targeting|Реклама ВКонтакте>\n<https://www.facebook.com/business/products/ads|Реклама Facebook>\n<https://target.my.com/|Реклама MyTarget>"
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
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/presentation/d/1K138Y8KYVKmJ5yud3elrwnce9z_yUvEnUUc3i2DXI9I/edit#slide=id.p|Знакомство с инструментами еЛама>\n <https://www.youtube.com/watch?v=zvxgBvSrbAI|Подробный обзор возможностей и инструментов еЛама>\n<https://help.elama.global/hc/ru/articles/360005932673-Обзор-нового-личного-кабинета|Ознакомься самостоятельно с интерфейсом еЛамы>\n\n+ Встреча\nКогда доходишь до пункта \"Встреча\", напиши об этом организатору в Slack"
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
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Для российского сегмента клиентов представляются акции по созданию/аудиту/копированию кампаний. В одной акции один домен может принять участие 1 раз. \n<https://secure.helpscout.net/docs/5b0fe61b2c7d3a0fa9a27457/article/5b0ff5d12c7d3a0fa9a2757f|Список акций, описание и условия>"
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
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://forms.gle/Eqx2nKtLQmEjdtnH7|Что делаем и сколько это стоит>"
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
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/document/d/1wRKMBfcj494dcsn8n4YZ7q34_DbIwRqT87JnMw-ywrI/edit|Получить доступы к рекламным системам (Я.Директ и Google Реклама)>"
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
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://elama.ru/pricing/|Информация о тарифах>"
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
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://elama.ru/partners/|Лендинг Партнерскойпрограммы>\n<https://elama.ru/info_static/uploads/files/18/19/part8.pdf|Условия Партнерской программы>\n\n+ Встреча "
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