import os
import time
import re
import slack

from slack import WebClient

client = slack.WebClient(token="xoxb-714578520370-719690847425-oB0mKbJGvWejGlGeyLs0uvR9")

client.chat_postMessage(
  channel="general",
  text="Test message"
)
