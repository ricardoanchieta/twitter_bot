from random import random
import tweepy
import time
from os import read, write

FILE_NAME = 'src/last_seen.txt'

def read_last_seen(FILE_NAME):
  file_read = open(FILE_NAME,'r')
  last_seen_id = int(file_read.read().strip())
  file_read.close()
  return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
  file_write = open(FILE_NAME, 'w')
  file_write.write(str(last_seen_id))
  file_write.close()
  return

def livros():
  livros = ['A insustentavel leveza do ser', 'O mundo de sofia', 'O alquimista','O caçador de pipas', 'Vidas secas',
            'Iracema','Dom casmurro', 'O perfume','Jogos vorazes','O lado bom da vida','Divina comedia de dante', 'Iliadas',
            'A hora da estrela','Crepusculo']
  p2 = [' é perfeito para momentos calmos', ', quando li me identifiquei bastante com o protagonista',' tenho certeza que vais gostar muito','. tu vai pegar muita gente lendo esse']

  indicacao = random.choice(livros) + random.choice(p2)
  return indicacao

def frases_sobiel():
  p1 = ['O flamengo', 'aiaia Meu anjo belga', 'Meu cartola', 'O vidal','Agora um time de verdade', 'Se o casimiro']
  p2 = [' é uma merda', ' é incrivel', ' vai jogar', 'amassa','nao for']
  p3 = [' muito desorganizado', ' hj passa o carro'," dos Demolay",' mengudo',' vasco']
  p4 = [" esse timinho"," humilhado", " no vasco",' eu sou um calhembeque bibi']
  p5 = [" teles estava certo", " eu falei ein", " sid tava la", " volta jorge jesus",' que leitura']
    
  frase_alea = random.choice(p1) + random.choice(p2) + random.choice(p3) + random.choice(p4) + random.choice(p5)
  return frase_alea

def resposta():
  read_last_seen_str = str(read_last_seen(FILE_NAME))
  mentions = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = 'extended')
  print('Ultimo ID pesquisado: ' + read_last_seen_str)
  for mention in mentions:

    tweet = api.get_status(mention.id);
    print(tweet.text.lower())
    print('Mention tweet found!')
    frase_sobis = frases_sobiel()

    store_last_seen(FILE_NAME, mention.id)

    print('@ desse cara aqui: '+ mention.user.screen_name)
    print('Mention.id: ' + mention.id_str)

    if True in [word in tweet.text.lower() for word in ['livro','livros'] ]:
      print('Indicando livros')
      livro = livros()
      api.update_status('@' + mention.user.screen_name + ' ' + livro, in_reply_to_status_id = mention.id)
    else:
      api.update_status('@' + mention.user.screen_name + ' ' + frase_sobis, in_reply_to_status_id = mention.id)
