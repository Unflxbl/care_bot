import os
import time
import re
import slack
from slack import WebClient
import flask
from flask import Flask, request, Response, make_response
from slackeventsapi import SlackEventAdapter

#Все это надо убрать в переменные окружения

client = slack.WebClient(token="xoxb-714578520370-719690847425-SoWwNC48UwKhTgLJPiEJGdmS")
SLACK_VERIFICATION_TOKEN = "c5vhYdFQdxgZexgbhPQXW3Ay"
SLACK_CLIENT_ID = "714578520370.726019560224"
SLACK_CLIENT_SECRET = "41a53e541c7495d7cb9192bfe075ab90"
SLACK_SIGNING_SECRET = "92d786a738a82418fb15ea97d501172d"

app = Flask(__name__)

slack_events_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, "/start", app)

def send_message(channel_id, message):
    client.chat_postMessage(
      channel=channel_id,
      text=message,
    )

@app.route('/', methods=['GET'])
def yes():
    """
    для проверки работы локалхоста
    """
    return Response('It works!')

"""
#Здесь мы валидируем домен для events, после валидации, если его не удалять, не работает ничего
@app.route("/start", methods=["GET", "POST"])
def hears():

    slack_event = request.get_json()

    # ============= Slack URL Verification ============ #
    # In order to verify the url of our endpoint, Slack will send a challenge
    # token in a request and check for this token in the response our endpoint
    # sends back.
    #       For more info: https://api.slack.com/events/url_verification
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type":
                                                             "application/json"
                                                             })

"""

@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    # If the incoming message contains "hi", then respond with a "Hello" message
    if "hi" in message.get('text'):
        send_message(channel_id="CM0GYQC7M", message="Hello!")

if __name__ == "__main__":
    app.run(debug=True)
