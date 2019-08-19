import os
import os
import time
import re
import slack

from slack import WebClient
import flask
from flask import Flask, request, Response

client = slack.WebClient(token="xoxb-714578520370-719690847425-7xvdRLMedjGdeLKQ152t41Gt")

app = Flask(__name__)

def send_message(channel_id, message):
    client.chat_postMessage(
      channel=channel_id,
      text=message,
    )

@app.route('/test', methods=['POST'])
def test():

    my_var = flask.request.values
    print(my_var)

    send_message(channel_id="CM0GYQC7M", message="Hello!")
    return Response(), 200

@app.route('/', methods=['GET'])
def yes():
    return Response('It works!')

if __name__ == "__main__":
    app.run(debug=True)
