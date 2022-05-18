from multiprocessing.connection import wait
from os import read, write
from random import random
import tweepy
import time
from src.functions import get_credencial

CREDENCIAL_FILE = 'src/credenciais.txt'

#login no bot
api_key = get_credencial(CREDENCIAL_FILE)[0]
api_secret_key = get_credencial(CREDENCIAL_FILE)[1]
access_token = get_credencial(CREDENCIAL_FILE)[2]
secret_access_token = get_credencial(CREDENCIAL_FILE)[3]

auth =  tweepy.OAuthHandler(api_key,api_secret_key)
auth.set_access_token(access_token,secret_access_token)

api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')

#funcao de responder mensoes
#pode apagar isso essa funcao aqui ainda to dev
def responder_mentions():
    mention = api.mentions_timeline()
    print(mention)

responder_mentions()



