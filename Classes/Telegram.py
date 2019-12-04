import requests


class Telegram:

    def __init__(self):
        self.botURL = 'https://api.telegram.org/bot914434782:AAFe0JjM6SQJBy21-2E9LdbKlV1kc2STMg8/getUpdates'

    def updater(self):
        return self