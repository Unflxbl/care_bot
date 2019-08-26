import json
import re
from flask import Flask, request, make_response
from slackeventsapi import SlackEventAdapter
from care_bot import Bot
from slack import WebClient

app = Flask(__name__)
careBot = Bot()


@app.route("/index", methods=["GET"])
def index():
    return "It Works!"


slack_events_adapter = SlackEventAdapter(careBot.verification, "/slack/events", app)

client = WebClient("insert token")

"""

Пока что это вообще не робит

@slack_events_adapter.on("message")
def event_handler(event_type, slack_event):
    if event_type == "message":
        # В переменную записываем текст из сообщение пользователя
        users_text = slack_event["text"]
        # В переменную записываем упоминание бота из текста пользователя, если оно есть
        bot_mention_match = re.search(careBot.user_id, users_text)
        # В переменную записываем было ли написано 'hello' пользователем в его сообщении
        hello_match = re.search('hello', users_text)
        if hello_match and bot_mention_match:
            return careBot.say_hello()
    return "No event handler found for %s type events" % event_type
"""


@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    emoji = event_data["event"]["reaction"]
    print(emoji)


@app.route("/slack/events", methods=["GET", "POST"])
def hears():
    # Понять что тут происходит
    response = json.loads(request.data)
    # Верификация URL
    if "challenge" in response:
        return make_response(response["challenge"], 200, {"content_type": "application/json"})
""""# Обработка событий из слака
    if "event" in response:
        event_type = response["event"]["type"]
        slack_event = response["event"]
        event_handler(event_type, slack_event)
        return make_response("Event HANDLED.", 200, )
    return make_response('Something went wrong :(', 404, {'X-Slack-No-Retry': 1})
"""

if __name__ == '__main__':
    app.run(debug=True)
