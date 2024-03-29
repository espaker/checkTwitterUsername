import requests


class Telegram:

    def __init__(self):
        self.botURL = 'https://api.telegram.org/bot914434782:AAFe0JjM6SQJBy21-2E9LdbKlV1kc2STMg8/'

    def updater(self):
        URL = '{}getUpdates'.format(self.botURL)
        headers = {'content-type': 'application/json', 'Accept': 'application/json'}
        try:
            r = requests.get(URL, headers=headers, timeout=60)
            if r.status_code in [200, 201, 202]:
                rjson = r.json()
                return rjson
            else:
                print('Não foi possível consultar o status: {}'.format(r.status_code))
        except requests.RequestException as err:
            print(err)
        except Exception as err:
            print(err)