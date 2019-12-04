import requests


class Twitter:

    def __init__(self):
        self.URL = 'https://twitter.com/users/username_available'

    def usernameCheckAvailability(self, username):
        URL = '{}?username={}'.format(self.URL, username)
        headers = {'content-type': 'application/json', 'Accept': 'application/json'}
        try:
            r = requests.get(URL, headers=headers, timeout=60)
            if r.status_code in [200, 201, 202]:
                rjson = r.json()
                return rjson
            else:
                print('Não foi possível consultar o username: {}'.format(r.status_code))
        except requests.RequestException as err:
            print(err)
        except Exception as err:
            print(err)