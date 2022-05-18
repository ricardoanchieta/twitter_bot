from multiprocessing.connection import wait
from os import read, write
from random import random
import tweepy
import time
from src.functions import get_credencial

CREDENCIAL_FILE = 'src/credenciais.txt'
LAST_SEEN_FILE = 'src/last_seen.txt'

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
def responder_mentions():
  read_last_seen_str = str(read_last_seen(FILE_NAME))
  mentions = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = 'extended')
  print('Ultimo ID pesquisado: ' + read_last_seen_str)
  for mention in mentions:
    print('Mention tweet found!')
    frase_sobis = frases_sobiel()
    store_last_seen(FILE_NAME, mention.id)
    api.update_status('@' + mention.user.screen_name + ' ' + frase_sobis, in_reply_to_status_id = mention.id)

while True:
    responder_mentions()
    time.sleep(15)



