def get_credencial(path_do_arquivo):
    f = open(path_do_arquivo,'r')
    credenciais = f.read()
    api_key = credenciais.split('\n')[0]
    api_secret_key = credenciais.split('\n')[1]
    access_token = credenciais.split('\n')[2]
    secret_access_token = credenciais.split('\n')[3]

    return api_key, api_secret_key, access_token, secret_access_token
