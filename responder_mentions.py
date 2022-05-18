
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
