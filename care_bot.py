import os
import time
import re
import slack

from slack import WebClient

client = slack.WebClient(token="xoxb-714578520370-719690847425-rpvmLyrfh2tn2yuu8Z5WcRbO")

client.chat_postMessage(
  channel="general",
  blocks=[
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Контекстная реклама: основы*"
      }
    },
    {
      "type": "divider"
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Знакомство с Яндекс.Директом\n <https://help.elama.global/hc/ru/articles/207432709|Прочитать>"
      },
      "accessory": {
        "type": "image",
        "image_url": "https://www.meme-arsenal.com/memes/148db78d7a53e8fe680408a6ad60c2c4.jpg",
        "alt_text": "лама"
      }
    },
    {
      "type": "divider"
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "Справился?"
        }
      ]
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "."
      },
      "accessory": {
        "type": "button",
        "text": {
          "type": "plain_text",
          "text": "Click Me"
        },
        "value": "click_me_123",
        "action_id": "button"
      }
    }
  ]
)

