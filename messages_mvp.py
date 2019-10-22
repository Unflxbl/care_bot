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
				"text": "*Знакомство с офисом и коллегами. Корпортал, Helpscout, Slack, Gmail. Помощь еЛамы для Заботы в Helpscout Docs*"
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
				"text": "*Про рабочий день, болезни, отпуск, регламенты работы*"
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
				"text": "*Что такое еЛама*"
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
				"text": "*Кто и чем занимается в Службе Заботы еЛама*"
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
				"text": "*Сделать небольшую презентацию о себе*"
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
				"text": "*Библиотека знаний*"
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
				"text": "*Контекстная реклама: Основы*"
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
				"text": "*Таргетированная реклама в соцсетях: Основы*"
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
				"text": "*Интерфейс и инструменты еЛамы*"
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
				"text": "*Акции для новых клиентов в еЛаме *"
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
				"text": "*Тест по услугам еЛама*"
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
				"text": "*Доступы к рекламным кабинетам в еЛама*"
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
				"text": "*Тарифы в еЛама*"
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
				"text": "*Партнерская программа в еЛаме *"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://elama.ru/partners/|Лендинг Партнерской программы>\n<https://elama.ru/info_static/uploads/files/18/19/part8.pdf|Условия Партнерской программы>\n\n+ Встреча "
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
				"text": "*Обзор рекламы в Директе* "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://www.youtube.com/watch?v=QL-vHIeUUlM|Реклама в Директе (в поиске и в сетях)>\n<https://www.yandex.ru/adv/edu/direct-start|Как разместить рекламу в Директе>\n<https://yandex.ru/support/direct/glossary.xml|Глоссарий>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Поисковые кампании*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Как настроить поисковую рекламу в Директе:\n<https://www.youtube.com/watch?v=wWtwW3ucuK8|Видео>\n<https://help.elama.global/hc/ru/articles/207445479|Инструкция> "
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Символы и операторы. Сервис подбора слов Wordstat. Минус-слова*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://yandex.ru/support/direct/keywords/symbols-and-operators.html|Символы и операторы ключевых фраз Директа>\n<https://ppc.world/articles/gajd-po-operatoram-yandeks-direkta/|Гайд по операторам Директа>\n<https://yandex.ru/support/direct/keywords/wordstat.html|Сервис подбора слов Wordstat>\n<https://yandex.ru/support/direct/keywords/negative-keywords.html|Минус-слова в Директе>\n<https://secure.helpscout.net/conversation/680703033/2089947|Пример письма 1>\n<https://secure.helpscout.net/conversation/781246108/2304468/|Пример письма 2>\n<https://goo.gl/forms/siDmdFJvVUOYvrzl2|Тест>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*РСЯ кампании*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://yandex.ru/support/direct/qanda/yan.html|Что такое Сети (РСЯ и внешние сети)>\n<https://www.youtube.com/watch?v=VHQxNHTlR5Q&list=PLjEKjSpX1kHVOqJ-uPl0j2hJZF-DDszFi|Вебинар про РСЯ>\n<https://yandex.ru/support/direct/efficiency/content-websites.xml|Как настроить РСЯ кампанию в Директе>\n<https://ppc.world/articles/nastrojka-kampanii-dlya-reklamnoj-seti-direkta/|Статья о настройке РСЯ>\n<https://www.youtube.com/watch?v=ABadItGsYi8|Правила и алгоритмы рекламы в РСЯ>\n<https://secure.helpscout.net/conversation/621377803/1946809/|Пример письма>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Исключение пересекающихся ключевых запросов - \"Кроссминусация\" в еЛаме*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://secure.helpscout.net/docs/5b0fe61b2c7d3a0fa9a27457/article/5cd027d72c7d3a177d6e6205/|Кроссминусация: что это и как работает>\n<https://help.elama.global/hc/ru/sections/201768901-Кросс-минусация|Статья в нашей помощи>\n<https://secure.helpscout.net/conversation/466037810/1557382/|Пример письма.Вложенные запросы, низкочастотные фразы, высокочастотные фразы>\nВстреча: Попробуйте объяснить своими словами как работает кроссминусация"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Модерация в Директе. Правила и требования к рекламе*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://yandex.ru/legal/general_adv_rules/|Правила и требования к рекламе на Директе-1>\n<https://yandex.ru/support/direct/moderation/adv-rules.html|Правила и требования к рекламе на Директе-2>\nРучная модерация:\n<https://secure.helpscout.net/docs/5b0fb9ae2c7d3a0fa9a27271/article/59b9519d2c7d3a73488cd57e/|Заявка в Яндекс>\n<https://secure.helpscout.net/docs/5b0fb9ae2c7d3a0fa9a27271/article/59e72c6604286370e4dc7b3b/|Гарантийные письма>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Что еще нужно знать*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/presentation/d/1PP73qasngVOijDkEbZ5alyJoBInEZf0PoxxmnxWze3o/edit#slide=id.g499dedcbba_0_43|Правила и особенности показа объявлений в Директе>\n<https://yandex.ru/adv/news/malo-pokazov-novyy-status-dlya-grupp-obyavleniy-v-direkte|Статус \"Мало показов\" в Директе>\n<https://secure.helpscout.net/conversation/792237895/2335741/|Пример письма>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Коммуникация с менеджером Яндекс Директа* "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/spreadsheets/d/1tRr3Vb4xdgbviOSVp6Xocb_tsdz_ix9UL7683r_WXTk/edit#gid=178158069|Связь со специалистами Яндекс Директа>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Тест*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/a/elama.ru/forms/d/e/1FAIpQLSfuve9b890-_U1xWmX9CtvxbIV2yJeSWAPBR4x7kpa0nxa6eg/viewform|Открыть>"
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
				"text": "*KeePass *"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5cde7dea0428634b855956ea|Устанавливаем программу KeePass с логинами и паролями для сотрудников еЛама>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Как писать письма*. *Где искать инфу в почте (тема, приветствие, шаблоны ответов)*.\n *Регламенты ответа. Заметки в Helpscout. Телефоны Яндекса, гугла, бухгалтерии. Пароли. Теги к письмам.* \n*Как писать в Яндекс по вопросам модерации и не только.* \n*Простая коммуникация с менеджером Яндекса по баллам, представителям, копированию c CTR*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/a/elama.ru/presentation/d/1uQvifLOfity_VyDGD0af6zMnHtsX0todyCMrlnZRDx0/edit?usp=sharing|Как писать письма, где искать информацию, что такое Helpscout>\n<https://docs.google.com/presentation/d/1UvI1k-Ccjcr1QX9MwR5fgOfmG592YYCcu8Cio18v9h0/edit#slide=id.p3|Как писать \"заботливые\" письма клиентам>\nКак искать что-либо в почте:\n<http://joxi.ru/Rmz1ZaNcWd95kr|1) Открыть>\n<http://joxi.ru/krDJM3GC0aNad2|2)Открыть  - можно найти инструкцию, переписку с клиентом, письмо и пр.>\n<https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe99942c7d3a2f9011a0f0/|Стандарты ответа на письмо>\n<https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe99dd2c7d3a2f9011a0f3/|Регламенты ответа на письмо>\n<https://docs.google.com/spreadsheets/d/177SFP21kdBXaJ-H7hJ4QwLhfczm2MGchNNGa15Hb0uY/edit#gid=0|Чек - лист по Helpscout. Вписывай фамилию и отмечай \"+\" или \"1\" то, что ты прошел>\nКоммуникация с другими отделами еЛама (почта, чат, телефон):\n<https://docs.google.com/document/d/1RRaQcq2piZWir6KepI4BhsCAiYVtLEvmygUj_TnG5AU/edit|Отдел продаж>\n<https://docs.google.com/document/d/1XMs8HT7dAuYdW6GHatz-mWUz5MNB_6S6nG9Z1eocKQU/edit|Разработка>\n<https://docs.google.com/document/d/1Q0e4bX3YpcvmO-MjhTb1sLi1zqf0U1hCc_4wh4bzR6k/edit|Маркетинг>\n<https://docs.google.com/document/d/13oI28c4-6Ur-nR0eTJfXpUGSI6LYSK6Ifk0SU5r1m_w/edit|HR>\n<https://docs.google.com/spreadsheets/d/1tRr3Vb4xdgbviOSVp6Xocb_tsdz_ix9UL7683r_WXTk/edit#gid=178158069|Почты для связи с рекламными системами>\nСообщи тим-лиду, что ты дошел до данного пункта и готов выйти на почту :)"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Простые письма и задачи: приглашения, копирование, модерация еЛамы, переводы ручные, автоматические письма от яндекса, клиент потерял пароль, простые письма клиентов *"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Для начала создай себе представительский аккаунт в Яндекс.Директе по этой <https://secure.helpscout.net/docs/5b0fb9ae2c7d3a0fa9a27271/article/5d527d770428631e94f94dd9/|инструкции>:\nПосле этого, напши свои логины тимлиду, для того, чтобы мы проверили всё ли сделано верно:)\nНачинаем делать простые письма и задачи. Регламент ответа клиенту - 4 рабочих часа\nФинансовые операции (переводы между аккаунтами, возвраты с контекстных систем)  делают только те, кто прошёл испытательный срок\n<https://docs.google.com/spreadsheets/d/1FU2RWbGKStmqs52bLdBUnAlW062GpaDbWTpIHQTMp-Q/edit#gid=0|Список стандартных писем, инструкции и шаблоны к ним. Список стоп-слов>\nПо возникающим вопросам тебе помогут сориентироваться инструкции в HelpScout и старые письма коллег (<http://joxi.ru/krDJM3GC0aNad2|Cкриншот как искать>)\nА также библиотека знаний с первого блока этого обучения и интернет :)\nЧем больше на этом этапе вы будете искать информацию, тем проще будет отвечать на более сложные письма в будущем. \nЕсли совсем не понятно ничего, не стесняйся - пиши в канал Slack \"новенькие-забота\"\n<https://docs.google.com/spreadsheets/d/1IPAcUJwdCCIR6C0xN_7leTBeM8lrRUEwuM3bowcQFrc/edit#gid=402245085|Примеры крутых ответов> (необязательно знать все темы, просто смотри на манеру общения, полноту ответов и так далее)"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Технические ошибки и баги. Инциденты *"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Что такое техническая бага и по каким параметрам ее определить\nКто занимается багой и как ее передать\nЧто проверить перед передачей баги и как прослеживать ее решение\n<https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5cdd6f380428634b85594b4c/|Инструкция>"
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
				"text": "*Аукцион и Ценообразование в Директ* "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://yandex.ru/adv/materials/auctiondirect|Аукцион Директа>\n<https://docs.google.com/a/elama.ru/presentation/d/1ArtZgccVGy0LF2pDYDJeKATCcbwGLNCaLJLrBPt4jU0/edit?usp=sharing|Ставки, цены, ранжирование объявлений в Директе>\n<https://yandex.ru/support/direct/troubleshooting/bidding.html|Объем трафика и ставки>\n<https://secure.helpscout.net/conversation/662228734/2047225/|Пример письма>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Стратегии размещения в Директе *"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://yandex.ru/support/direct/strategies/select-strategy.xml|Стратегии (ручная и автоматические)>\n<https://help.elama.global/hc/ru/articles/207746049-Стратегии-управления-ставками-в-Яндекс-Директе-какую-выбрать|Какую стратегию выбрать?>\nОтметим, что клиенты еЛама чаще всего используют ручную стратегию, чтобы можно было воспользоваться нашим инструментом (бидером)\n<https://secure.helpscout.net/conhversation/817885853/2401788/ttps://secure.helpscout.net/conversation/558228156/1787009/|Пример письма>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Автоматическое управление ставками еЛама или Бид-менеджер или Бидер*\n*Доп.настройка \"Сео-бидер\" для управления ставками* "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/document/d/1KGPIEIvzHnK1cPQQnACyK_183JrMeJ9bFbJWc3aFTA4/edit|Бидер для Директа: как настроить и особенности>\n<https://docs.google.com/document/d/1KGPIEIvzHnK1cPQQnACyK_183JrMeJ9bFbJWc3aFTA4/edit|Бидер для Директа: как настроить и особенности>\n<https://docs.google.com/document/d/1fnW4eDYOt0naMmdtAG447xAOA0Y7eeFb-4ntQLq4P48/edit|Бидер для Google Ads: как настроить и особенности>\n<https://help.elama.global/hc/ru/sections/201785122-Автоматическое-управление-ставками|Инструкции по настройке бидера в еЛама>\n<https://secure.helpscout.net/conversation/798594783/2350215/|Пример письма>\n<https://secure.helpscout.net/conversation/830994043/2437704/|Пример письма>\n<https://secure.helpscout.net/conversation/792404070/2336015/|Пример письма>\n<https://secure.helpscout.net/conversation/833686970/2443430/|Пример письма>\n<https://secure.helpscout.net/conversation/788145864/2325411/|Пример письма>\nЭто внутренний инструмент еЛама для просмотра включения, отключения и времени работы бидера:\n<https://customer-care.bidmanager.elama.ru/|Мониторинг работы биддера>\nДоп.настройка \"Сео-бидер\" для управления ставками (в новом нет)\n<https://www.youtube.com/watch?v=d4ntdJTMfTY|Сео-бидер>\n<https://secure.helpscout.net/conversation/704249191/2146660/|Пример письма>\n<https://help.elama.ru/hc/ru/articles/208701945|Для чего нужны API баллы Яндекс Директа>\n<https://secure.helpscout.net/docs/5b0fb9ae2c7d3a0fa9a27271/article/5b0fbc820428632c466a5e6c|бидер в том числе расходует баллы api в аккаунте>\n<https://secure.helpscout.net/conversation/722663462/2185120/|Пример письма>\n+ Встреча\nОчень важная тема, перед встречей нужно все прочитать/посмотреть и постараться вникнуть в этот инструмент.\nЕсли есть вопросы, подготовь их к этой встрече :)"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*UTM-разметка*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/document/d/1zQgHX4rn2TomBOKbb3TB7YO34iEH-0kIt-rpQyKPGyg/edit|Что это и как работает>\n<https://help.elama.global/hc/ru/sections/201738062-UTM-метки|Как добавить UTM-метки через еЛама>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Практика: Создать рекламные кампании в Директе*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Вам нужно будет создать три кампании и использовать инструменты еЛамы.\nЕсли задание выполнено, укажи логин аккаунта в Директе elama-xxxxxxx\nИ не забудь отправить кампании на модерацию\n<https://docs.google.com/document/d/1I2fb23lwUefHyfFch7g07mfD68fxnhAcbi5trIdwLyU/edit?usp=sharing|Задание и инструкции по ссылке>\nРабота с Коммандером\nЗадание: создать кампании Поиск и РСЯ, используя коммандер\n<https://yandex.ru/support/direct-commander-new/campaigns/add.html|Как создать кампании>\n<https://yandex.ru/support/direct-commander-new/adgroups/add.html|Как добавить группы>\n<https://yandex.ru/support/direct-commander-new/ads/add.html|Как добавить объявления>\nПосле создания кампаний и отправки их на сервер \n<https://yadi.sk/d/Iht1Eyrn3SEqoR|Проверь кампании через Чек-лист>\nИтого, всего должно быть 5 кампаний"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Тест 2 *"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/a/elama.ru/forms/d/e/1FAIpQLSfgDdDEdQUNwnsg5M7ZCZivAEuUU_eNR6UQsXDUagQHHt4gQw/viewform|Тест 2>"
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
				"text": "*Обзор рекламы Google Ads*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://help.elama.global/hc/ru/articles/207445309-Что-такое-Google-AdWords|Реклама в Google (типы кампаний)>\n<https://support.google.com/adwords/answer/2567043?hl=ru&co=ADWORDS.IsAWNCustomer%3Dtrue|Оф. спрaвка>\n<https://support.google.com/google-ads/topic/3121777|Глоссарий>\n"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Типы соответствия. Планировщик ключевых слов. Минус-слова *"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://youtu.be/qyOCPc5XzWc|Типы соответствия ключевых слов (символы и операторы)>\n<https://elama.ru/blog/kak-sostavit-spisok-klyuchevyh-slov-v-google-adwords/|Планировщик ключевых слов>\n<https://support.google.com/google-ads/answer/2453972?hl=ru|Минус-слова в Google>\n<https://secure.helpscout.net/conversation/607504976/1909542/|Пример письма>\n<https://secure.helpscout.net/conversation/666203146/2056024/|Пример письма>\n<https://secure.helpscout.net/conversation/756057638/2248436/|Пример письма>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Правила показа*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://support.google.com/adwords/answer/1704373?hl=ru|Где покажется реклама в Google >\n<https://www.youtube.com/watch?v=oZ_LLkBy6d8|Показатель качества>\n<https://support.google.com/adwords/answer/1722122?hl=ru|Ранжирование (позиция и рейтинг)>\n<https://secure.helpscout.net/conversation/759169362/2253990/|Пример письма>\n<https://secure.helpscout.net/conversation/668530704/2060790/|Пример письма>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Ценообразование в Google Ads. Ставки, Рейтинг, и Аукцион на Поиске и КМС* "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/a/elama.ru/presentation/d/1kZD08CgKgwmkvEkXRnG9n5ClztPV7Bx10EUqCmK2nbI/edit?usp=sharing|Ценообразование, ставки, аукцион  в Google>\n<https://support.google.com/adwords/answer/142918?hl=ru|Аукцион на поиске>\n<https://support.google.com/adwords/answer/1752122?hl=ru|Рейтинг объявления>\n<https://support.google.com/adwords/answer/7050591?hl=ru|Показатель качества ключевых фраз>\n<https://support.google.com/adwords/answer/6326?hl=ru|Максимальная ставка>\n<https://support.google.com/adwords/answer/2996564?hl=ru|Аукцион КМС>\n<https://support.google.com/adwords/answer/2454058?hl=ru|Выбор ставки для КМС>\n<https://secure.helpscout.net/conversation/842925797/2465585/|Пример письма>\n<https://secure.helpscout.net/conversation/838032996/2456232/|Пример письма>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Поисковые кампании*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://www.youtube.com/watch?v=kWCI9THjT68&t=48s|Как настроить поисковую кампанию в Google>\n<https://www.youtube.com/watch?v=mxrxsfxxXi4|\"Шаблоны\" в Google>\n<https://secure.helpscout.net/conversation/661919766/2046560/|Пример письма>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*КМС кампании*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://www.youtube.com/watch?v=iuyWtE_K6NI|Как настроить КМС кампанию в Google>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Модерация в  Google Ads. Правила и требования*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://support.google.com/adwordspolicy/answer/6008942?hl=ru|Правила и требования к рекламе в Google>\n<https://secure.helpscout.net/docs/5b0fcc0a0428632c466a5ef8/article/5b0fd0290428632c466a5f1c|Модерация в Google>\n<https://docs.google.com/presentation/d/1HpyXhUsRpYlmYO26IoJV33YDyLJOjQ1b/edit#slide=id.p1|Модерация: основные причины отклонения>\n<https://docs.google.com/spreadsheets/d/1tRr3Vb4xdgbviOSVp6Xocb_tsdz_ix9UL7683r_WXTk/edit#gid=178158069|Связь со специалистами>\nВ качестве контактной почты вставляйте milo@elama.ru + Ваше имя\nДобавляйте в комменте просьбу указать идентификатор аккаунта в ответном письме"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Адреса в объявлениях в Google Ads* "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://ppc.world/articles/kak-sinhronizirovat-google-moy-biznes-i-adwords/|Как добавить адреса в объявления AdWords из Google Мой Бизнес>\n<https://support.google.com/google-ads/answer/7189290|Оф. Справка>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Google Merchant*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://support.google.com/merchants/answer/188493?hl=ru&ref_topic=7287851|Что такое Google Merchant>\n<https://support.google.com/merchants/answer/6159060?hl=ru|Как связать аккаунты Google Merchant Center и Google Ads>\n* Пример кампаний настроенных на основе данных в Google Merchant в аккаунте клиента - 831-302-9812\n<https://secure.helpscout.net/conversation/85/1928398/2482139|Пример письма  (13 мая)>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Практика: Создать рекламные кампании в Google Ads*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/document/d/1iaFvixFU1_J096GSBQynTBasL79k4Vrxc2trmTUwkOI/edit|Задание и инструкции>\nЕсли задание выполнено, укажи иденификатор аккаунта. - надо придумать че сделать\n<https://secure.helpscout.net/docs/5b0fcc0a0428632c466a5ef8/article/5b0fce1b0428632c466a5f0a/|+ скопировать одну из твоих кампаний Яндекс.Директа в Google Ads, используя инструкцию>\nт.е. у тебя должно быть ТРИ кампании и не забудь настроить инструменты для кампаний в еЛаме"
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
				"text": "*Подключение к чату на сайте. Общение с клиентами в чате *  "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe99dd2c7d3a2f9011a0f3/|Регламенты ответа на чат>\n<https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe99b10428635ba8b2702f|Стандарты ответа на чат>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Тест 3*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/a/elama.ru/forms/d/e/1FAIpQLSftRzqb_lu-KsaLdoPo3DykZ_qEJ3ke3w8B8x5RjzE03YERAg/viewform|Тест 3>"
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
				"text": "*Вконтакте* "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://vk.com/ads?act=office_help&oid=-19542789|Основы таргетированной рекламы в ВК (все до пункта 2.5)>\n<https://ppc.world/articles/nastroyka-targetirovannoy-reklamy-vo-vkontakte-poshagovaya-instrukciya/|Настройка рекламы в Вконтакте>\n<https://www.youtube.com/watch?v=oh-q61Q-pgA|Форматы размещения, Аукцион, Кейсы>\n<https://elama.ru/blog/darim-dostup-k-cerebro-target/|Об инструменте Церебро для ВК>\n<https://pl.elama.ru/cerebro_target|Акция по Церебро от Еламы>\n<https://secure.helpscout.net/docs/5b0fe0950428632c466a5fc0/article/5b0fe0d70428632c466a5fc9/|Как создать клиенту рекламный аккаунт в ВК>\n<https://secure.helpscout.net/docs/5b0fe0950428632c466a5fc0/article/5b0fe0c62c7d3a0fa9a27403/|Как выдать доп. доступ к кабинету ВК><http://joxi.ru/xAegE4wCR6WDOm|Баланс на ВК>\nПо стандарту в общем лимите ВК от еЛама лежит 100 рублей + переведенные деньги клиента\nПри переводе НДС не списывается, т.к. НДС включается в ценку клика\n<https://docs.google.com/spreadsheets/d/1tRr3Vb4xdgbviOSVp6Xocb_tsdz_ix9UL7683r_WXTk/edit#gid=178158069|Связь со специалистами ВК>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Facebook Часть 1 *"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://help.elama.global/hc/ru/articles/360003227793|Преимущества и особенности работы с Фейсбуком через еЛама>\n<https://elama.ru/blog/8-shagov-dlya-zapuska-targetirovannoy-reklamy-v-facebook/|8 шагов для запуска таргетированной рекламы в Facebook>\n<https://docs.google.com/presentation/d/1SxUaOcMre4RVx91tZqNr_irme-PRXuTw7ed-og51KzA/edit#slide=id.g46a3a100ed_0_171|Фейсбук для начинающих>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Facebook Часть 2* "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/presentation/d/1KRiOe8L0sC41079d7HLPaYWOwUJQ66JtvwOEbvOfVQo/edit#slide=id.p|Правила рекламы>\n<https://docs.google.com/presentation/d/1ebaOIrG0C0ROec364dishv0V9OI9dgDuWWjVPOyQH9s/edit#slide=id.p4|Аукцион>\n<https://docs.google.com/presentation/d/1fYIbgmX28ArhYv_jeBYyfvATjqlgbmAzM19ti-_BRfE/edit#slide=id.g37454f842b_0_441|Аудитории>\n<https://docs.google.com/presentation/d/16wY80k4AxxBb7_IqtCpij_f8atTqWrxB4aK7o5xG5bc/edit#slide=id.g3673ae8bd1_0_45|Пиксель>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Facebook Часть 3 *"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://youtu.be/0KSitdYKie4|Основы эффективной рекламы в Facebook>\n<https://docs.google.com/presentation/d/1jXlM1F5RRBHjCIvGMFxMNxP5_kgLBvjps-_jM7zQuwY/edit#slide=id.g4829e6cb0a_0_0|Самые часто задаваемые вопросы  по Facebook>\n<https://docs.google.com/document/d/1SNqaA_V09z48tS9jVn-Y0jlfFD4ML-PVEReJZu6IT6Q/edit|Кейсы для ознакомления>\n<https://docs.google.com/forms/d/e/1FAIpQLSenNIQs1_5Eei1VJMwwLVOxqnFIBj6RdwN4OpomQ9cq2KQ3kQ/viewform|Тест>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*MyTarget*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://help.elama.global/hc/ru/articles/115004173954|Как запустить первую кампанию в MyTarget>\n<https://www.youtube.com/watch?v=kmbFlad-R_s|Секреты привлечения клиентов из социальных сетей><https://secure.helpscout.net/docs/5b0fe0540428632c466a5fbb/article/5b0fe0780428632c466a5fbe/|Как создать клиенту рекламный аккаунт в МТ>\n<http://joxi.ru/gmvpOxDcqBpP4A|Баланс на МТ>"
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
				"text": "*Основы работы с Яндекс.Метрикой*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://yandex.ru/adv/edu/metrika-start|Базовые понятия. Как Метрика собирает и обрабатывает данные.Как самостоятельно подключать и настраивать счётчики>\n<https://secure.helpscout.net/docs/5b0fb9ae2c7d3a0fa9a27271/article/5b0fca9b0428632c466a5ee8|Как связать Директ с Метрикой>\n"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Я.Метрика. Счетчик Я.Метрики*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://www.youtube.com/watch?v=LAeX9iCSvUs&t=310s|Как анализировать рекламу и повышать эффективность с помощью Яндекс.Метрики>\n<https://secure.helpscout.net/docs/5b0fb9ae2c7d3a0fa9a27271/article/5cb9ba722c7d3a026fd3d33a/|Как проверить, корректно ли работает счетчик у клиента>\n"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Сегменты Метрики* "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://yandex.ru/support/metrika/general/segmentation.xml |Что такое Сегментация данных>\n<https://elama.ru/blog/kak-segmentirovat-trafik-v-yandeks-metrike/|Для чего нужны сегменты и как их создать>\n<https://yagla.ru/blog/analitika/segmenty-v-yandeksmetrike/|Еще информация о сегментах>\n<https://secure.helpscout.net/conversation/700312602/2137610/|Пример письма>\n"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Цели Метрики*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://yandex.ru/support/metrika/reports/add-goals.xml|Что такое цели Метрики>\n<https://ppc.world/articles/poshagovaya-instrukciya-dlya-nastroyki-celey-v-yandeksmetrike/|Типы и настройка целей>\n<https://secure.helpscout.net/conversation/830734679/2436540/|Пример письма>\n<https://secure.helpscout.net/conversation/699572978/2136905/|Пример письма>\n"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Отчеты Метрики*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://yandex.ru/support/metrika/reports/overview.html|Обзор отчетов>\n<https://help.elama.global/hc/ru/articles/115000158785-Как-настроить-отчеты-в-Яндекс-Метрике|Инструменты формирования отчетов>\n<https://yandex.ru/support/metrika/reports/report-general.xml|Еще информация об отчетах>\n"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Особенности статистики в Директе и в Метрике *"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://secure.helpscout.net/docs/5b0fb9ae2c7d3a0fa9a27271/article/5b0fcac70428632c466a5eea/|Почему данные в Директе и в Метрике могут не сходиться-1>\n<https://elama.ru/blog/osobennosti-statistiki-po-reklamnym-kampaniyam-v-direkte-i-metrike/|Почему данные в Директе и в Метрике могут не сходиться-2>\n<https://secure.helpscout.net/conversation/764656455/2265082/| Пример письма-1>\n<https://secure.helpscout.net/conversation/846717816/2471490| Пример письма-2>\n<https://secure.helpscout.net/conversation/806272736/2371347| Пример письма-3>\n"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Вебвизор*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://yandex.ru/support/metrika/general/counter-webvisor.xml|Что такое Вебвизор>\n<https://metrika.yandex.ru/promo/webvisor|Для чего нужен Вебвизор и Как им пользоваться>\n<https://elama.ru/blog/kak-polzovatsya-vebvizorom//|Для чего нужен Вебвизор и Как им пользоваться-2>\n<https://secure.helpscout.net/conversation/824522210/2420538|Пример письма-1>\n<https://secure.helpscout.net/conversation/771103311/2281126/|Пример письма-2>\n"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Скликивание, высокий процент показов*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/presentation/d/17JWqSpHGiRHabS8j0pv-1dbzAeiYf9fxWKxO25oARNo/edit#slide=id.p|Как действовать в том случае, если у клиента возник сложный вопрос, и чем может помочь Метрика>\n"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Ретаргетинг  и Подбор аудитории в Директе *"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://yandex.ru/support/direct/impression-criteria/retargeting-lists.html|Что такое Ретаргетинг>\n<https://yagla.ru/blog/kontekstnaya-reklama/retargeting-v-yandeksdirekt/|Как настроить и анализировать Ретаргетинг>\n<https://secure.helpscout.net/conversation/827285061/2427037/|Пример письма-1>\n<https://secure.helpscout.net/conversation/754543860/2244241/ |Пример письма-2>\n<https://secure.helpscout.net/conversation/749044718/2233685/|Пример письма-3>\n"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Я.Аудитории*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://yandex.ru/support/audience/|Что такое Я.Аудитории>\n<https://www.youtube.com/watch?v=UcQIz1vsSqw|Типы сегментов Я.Аудитории>\n<http://audience-checker.elama.zone/|Инструмент для сотрудников еЛама, который проверяет и исправляет файл аудитории на основе загружаемых данных>\n<https://secure.helpscout.net/conversation/620171110/1945070/|Пример письма-1>\n<https://secure.helpscout.net/conversation/657788240/2036368/?folderId=1662200|Пример письма-2>"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Тест 4*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/a/elama.ru/forms/d/e/1FAIpQLSeVHVLAQO92PsqooPcn4FoW1MbQMZgo-0VVi5jY5bNPM59M8w/viewform|Тест 4>"
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
				"text": "*Подготовка к телефону*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Сообщи Свете, что ты дошел до данного пункта и готовишься выйти на телефон :)\nУбедись, что все пункты выше успешно тобой выполнены\nСообщи Алене, что тебя нужно зарегистрировать в CRM и Mango Office\nАлена расскажет, как и зачем пользоваться CRM и Mango Office\n\nПосле того, как получишь доступы, посмотри инструкцию: \n<https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5d5d48642c7d3a7920be51c7|Как работать с amoCRM>\nВнутренняя работа с тарифами Basic и Optimal\nЕсли тариф клиента не определен, и перед звонком ты слышишь автосообщение \"Нам не удалось определить аккаунт по номеру телефона\", то нужно уточнить у звонящего его ID и проверить тариф\n<https://new.elama.ru/admin/plan|Ссылка на инструмент проверки тарифа>\n<http://joxi.ru/DrlgldDCV5wvwA|Как это выглядит>\n\nТариф Optimal мы консультируем, а вот тариф Basic просим написать на почту и объясняем, почему.\nПосле разговора не забудь занести ID пользователя в CRM, чтобы в будущем мы могли отфильтровать его сразу.\n"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Подготовка*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Повторить:\n<https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/category/5afe99cd2c7d3a2f9011a0f2|1) Регламенты>\n<https://secure.helpscout.net/docs/58c11eb8dd8c8e56bfa84fdf/article/5afe99590428635ba8b2702c/|2) Стандарты>\n<https://docs.google.com/presentation/d/1WQMh6tkWgfLibhLnF02GA9-dVsZ0pcq7/edit#slide=id.p1|3) Презентация (после обучения)>\n"
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
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<http://vseklass.ru/obshhenie/kak-nauchitsya-pravilno-razgovarivat-po-telefonu.html|Телефонный этикет>\n<https://docs.google.com/presentation/d/1MGS_Um4UfK3MlaZKCfhOu_Eby4QeYqqfcqtDebKwzbE/edit?usp=sharing|Телефонный этикет-2>\n<https://docs.google.com/presentation/d/1yRRiF9rtZjA8Z8iFa4xOKxvmZm7ZScBAPhhAlDzTts8/edit#slide=id.p|Как говорить, ставить на удержание, переводить на сотрудника>\n<https://miro.com/app/board/o9J_kxg5Dro=/|Добавочные коллег и сфера их деятельности>\nНа нашу бухгалтерию переводить клиентов ни в коем случае нельзя (!!!)\n<https://docs.google.com/document/d/1RRaQcq2piZWir6KepI4BhsCAiYVtLEvmygUj_TnG5AU/edit|Регламенты перевода на продажи>\n"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Разговоры. Записи разговоров* "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Послушать записи разговоров. Определить, что было хорошо, что не очень:\n1. https://yadi.sk/d/vHdrUH6N3JAcaU - 0:20  -  Хорошо ли поставлено удержание? 1:30 - Хoрошо ли снято?\n2. https://yadi.sk/d/W8GAP1Yf3JAeef  - Оцените разговор в целом\n3. https://yadi.sk/d/WYaIr5Lu3JAfkd - Удобный ли способ получения информации был предложен клиенту, вежливо ли поздоровались?\n4. https://yadi.sk/d/ZmGMwsuW3JAfuA  - Что делать, если клиента не слышно\n5. https://yadi.sk/d/fA5N_XMU3JAZof - Обратите внимание на интонацию, внимательно прослушайте моменты на 0:24, 0:39, 1:20, 1:48, 2:11, 2:17. Были ли слова паразиты, вежливо ли звучали ответы специалиста, корректно ли поставили на удержание клиента?\n6. https://yadi.sk/d/juXmqWlz3JAZNQ - на 0:40 клиент просит отправить электронные версии закрывающих на почту. Можно ли было предложить клиенту другой, более удобный способ получения документов?\n7. https://yadi.sk/d/ECCjLIcXaV3JAi - Присутствует ли нисходящая интонация у специалиста? Как было бы лучше ответить?\n8. https://yadi.sk/d/NNI7LwMP3JAbnW - 0:23, 1:18. - Какие ошибки Вы услышали?\n9.https://yadi.sk/d/C9Nfeiqr3JAcC3 - с 0:24 - Как лучше было поставить на удержание?\n10.https://yadi.sk/d/JqrjEQJn3JAcLp - Какие ошибки Вы нашли?\n"
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
				"text": "*Системы Коллтрекинга* "
			},
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://elama.ru/blog/chto-takoe-kolltreking-i-zachem-ego-ispolzovat/|Что такое Коллтрекинг>\n<https://ppc.world/articles/sistemy-kolltrekinga-chto-zachem-pochem/|Системы Коллтрекинга и их особенности>\nВ еЛама можно подключить оплату следующих систем:\n <https://calltracking.ru|Calltrackung.ru>\n<https://www.calltouch.ru|Calltouch>\n\n<https://yandex.ru/support/metrika/general/target-call.xml|Целевой звонок Яндекса>\n<https://support.google.com/google-ads/answer/6100664|Отслеживание звонков-конверсий Гугл>"
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
				"text": "*Имиджевая реклама: стимулирование спроса *"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://yandex.ru/support/direct/products-cpm-campaign/about.html|Медийные баннеры>\n<https://yandex.ru/support/direct/products-cpm-campaign-video/about.html|Видеореклама>\n<https://yandex.ru/support/direct/products-cpm-campaign-frontpage/about.html|Медийный баннер на Главной>\n<https://yandex.ru/support/direct/products-cpm-campaign-outdoor/about.html|Наружная реклама>\n<https://yandex.ru/support/direct/products-text-image-ads/types.html|Текстово-графические объявления>\n"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Performance-реклама: от спроса к продажам*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://yandex.ru/support/direct/products-image-ads/about.html|Графические объявления>\n<https://yandex.ru/support/direct/products-video-ads/about.html|Видеообъявления>\n<https://yandex.ru/support/direct/products-mobile-apps-ads/about.html|Реклама мобильных приложений>\n<https://yandex.ru/support/direct/features/dynamic-text-ads.xml|Динамические объявления>\n<https://yandex.ru/support/direct/products-media-context-banner/about.html|Баннер на поиске (МКБ)>\n"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Персонализированная реклама: возврат клиентов и доппродажи*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://yandex.ru/support/direct/smart-banners/about.html|Смарт-баннеры>\n"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Я.Справочник*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://yandex.ru/support/sprav/ |Что такое Я.Справочник>\n<https://www.youtube.com/playlist?list=PLo3X_vMPl8XjSli-81dTQzUTs5W|Видео про Cправочник>\n<https://secure.helpscout.net/docs/5b0fb9ae2c7d3a0fa9a27271/article/5b840e3a2c7d3a03f89e268f/|Как подключить Я.Справочник к еЛаме>\n"
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
				"text": "*Google Analytics* "
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
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/presentation/d/1FywhXWhGywW7XRgIRA9__Lb3inpKnQCVOOe2hwWlDOA/edit#slide=id.p3|Что такое Google Analytics, как связать с аккаунтом AdWords, анализ данных-1>\n<https://www.youtube.com/watch?v=Jv6OWhVh8rc&index=1&list=PLm4rB-wmRQyyhH5PBCZiUOKFao_bhcrRP|Что такое Google Analytics, как связать с аккаунтом AdWords, анализ данных-2>\n<https://www.youtube.com/watch?v=xmuTyUDw1Lg|Анализируем рекламу и повышаем ее эффективность с помощью Google Analytics>\n"
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
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://secure.helpscout.net/conversation/323252246/1237612?folderId=568624|Что это за инструмент и зачем он нужен>\n<https://help.elama.global/hc/ru/articles/205898712|Что такое выгрузка о расходах>\n<https://help.elama.global/hc/ru/articles/205834761|Как настроить>\n<https://support.google.com/analytics/answer/2649554?hl=ru&ref_topic=1009620|Что такое ресурс> \n<https://support.google.com/analytics/answer/2649553?hl=ru|Что такое представление>\n<https://secure.helpscout.net/conversation/647684043/2010728/|Пример письма-1>\n<https://secure.helpscout.net/conversation/801602456/2359508/|Пример письма-2>\n<https://secure.helpscout.net/conversation/615579334/1931814/|Пример письма-3>\n"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Ремаркетинг в Google AdWords*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://www.youtube.com/watch?v=KLivohOtQdA|Что такое Ремаркетинг и Как настроить>\n<https://support.google.com/adwords/answer/2453998?hl=ru|Преимущества и Виды>\n<https://secure.helpscout.net/conversation/829665475/2434457|Пример письма>\n"
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
				"text": "*Вопросы к экзамену *"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://docs.google.com/document/d/1U_Y73RVjPlDgkdesrDqjQaF-RDgsaUhBaiLZc4AI_qU/edit|Вопросы к экзамену>"
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
				"text": "*Что дальше?*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "И вот ты прошел испытательный срок, но обучение на этом не заканчивается :)\nПериодически тебе будут приходить обязательные тесты на рабочую почту Gmail.Просьба не пропускать и отвечать правильно на вопросы\n А ниже находятся материалы для подготовки к обязательной сдаче сертификации.\n Какой-нибудь из сертификатов сдается раз в квартал"
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
