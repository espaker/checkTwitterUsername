# -*- coding: utf-8 -*-
#######################################
####### Check Twitter Username ########
#######################################
#                _._                  #
#            __.{,_.).__              #
#         .-"           "-.           #
#       .'  __.........__  '.         #
#      /.-'`___.......___`'-.\        #
#     /_.-'` /   \ /   \ `'-._\       #
#     |     |   '/ \'   |     |       #
#     |      '-'     '-'      |       #
#     ;                       ;       #
#     _\         ___         /_       #
#    /  '.'-.__  ___  __.-'.'  \      #
#  _/_    `'-..._____...-'`    _\_    #
# /   \           .           /   \   #
# \____)         .           (____/   #
#     \___________.___________/       #
#       \___________________/         #
#      (_____________________)        #
#                                     #
# - Desenvolvido por Espaker Kaminski #
#######################################

import requests

from Classes.Parser import Parser
from Classes.Mail import Mail
from Classes.Utils import Utils


if __name__ == "__main__":
        usernames = ['espaker', 'leonardson']

        while True:
            for user in usernames:
                URL = 'https://twitter.com/users/username_available?username={}'.format(user)
                headers = {'content-type': 'application/json', 'Accept': 'application/json'}
                try:
                    r = requests.get(URL, headers=headers, timeout=60)
                    if r.status_code in [200, 201, 202]:
                        rjson = r.json()
                        print(rjson)
                    else:
                        print('Não foi possível consultar o username: {}'.format(r.status_code))
                except requests.RequestException as err:
                    print(err)
                except Exception as err:
                    print(err)
