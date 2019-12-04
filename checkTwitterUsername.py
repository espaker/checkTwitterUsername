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
import os
import sys
import logging
import threading
import signal
import time

from logging.handlers import RotatingFileHandler

from Classes.Parser import Parser
from Classes.Mail import Mail
from Classes.Utils import Utils
from Classes.Telegram import Telegram
from Classes.Twitter import Twitter

app_version = '1.0.1'


def getUpdates(telegram):
    try:
        lastState = None
        while True:
            state = telegram.updater()
            if state != lastState:
                print(state)
            lastState = state
            time.sleep(15)

def getUsernamesStatus(twitter):
    try:
        while True:
            usernames = ['espaker', 'leonardson', 'espaker101']
            for username in usernames:
                status = twitter.usernameCheckAvailability(username)
                if status.get('valid'):
                    print(status)
            time.sleep(300)


def initiate():
    log_main.info('Iniciando a checkTwitterUsername versão: {}'.format(app_version))

    signal.signal(signal.SIGTERM, finalize)
    signal.signal(signal.SIGINT, finalize)


    if len(sys.argv) > 1:
        if sys.argv[1] in ('-v', '--version'):
            print('checkTwitterUsername')
            print('Versão: {}'.format(app_version))
            sys.exit(0)
        else:
            print('ERRO | Parâmetro desconhecido: {}'.format(sys.argv))
            sys.exit(2)
    else:
        # Instanciando e iniciando thread de updates do telegram
        telegram = Telegram()
        tlg = threading.Thread(target=getUpdates, args=(telegram,))
        tlg.start()

        # Instanciando e iniciando thread de checagem do twitter
        twitter = Twitter()
        tt = threading.Thread(target=getUsernamesStatus, args=(twitter,))
        tt.start()

        while True:
            print('Rodando')
            time.sleep(5)
        sys.exit(1)

def finalize(signum, desc):
    log_main.info('Recebi o sinal [{}] Desc [{}], finalizando...'.format(signum, desc))
    sys.exit(0)

if __name__ == "__main__":
    workdir = Utils.get_workdir()
    conf = Parser(os.path.join(workdir, 'config.ini')).conf_get()
    _level = conf.getint('Debug', 'Level', fallback=3)
    debug_dir = os.path.join(workdir, 'debug')
    log_file_path = os.path.join(debug_dir, 'checkTwitterUsername.log')
    if not os.path.exists(debug_dir):
        os.mkdir(debug_dir, 0o775)
    log_handler = RotatingFileHandler(log_file_path, maxBytes=1024 * 1024 * 10, backupCount=10)
    log_handler.setLevel(logging.DEBUG)
    log_handler.setFormatter(logging.Formatter('[%(asctime)s] | %(levelname)s | %(name)s | %(message)s'))
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(log_handler)
    log_main = logging.getLogger('checkTwitterUsername:' + str(os.getpid()))

    initiate()
