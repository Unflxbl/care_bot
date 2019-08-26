from slack import WebClient

# Это надо убрать в переменные окружения
client_id = "714578520370.726019560224"
client_secret = "41a53e541c7495d7cb9192bfe075ab90"
verification = "92d786a738a82418fb15ea97d501172d"

class Bot(object):
    def __init__(self):
        super(Bot, self).__init__()
        self.oauth = {"client_id": client_id,
                      "client_secret": client_secret,
                      "scope": "bot"}
        self.verification = verification
        self.client = WebClient("")

    def auth(self, code):
        auth_response = self.client.oauth_access(client_id=client_id, client_secret=client_secret, code=code)
        self.user_id = auth_response["bot"]["bot_user_id"]
        self.client = WebClient("xoxb-714578520370-719690847425-htjml7V6tIeI9njSBLQ0p9p0")

    def say_hello(self, message):
        channel = message["channel"]
        hello_message = "I want to live! Please build me"
        self.client.chat_postMessage(
            channel=channel,
            text=hello_message,
        )