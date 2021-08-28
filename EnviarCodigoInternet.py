def mandar_api(texto):
    # Chave da API
    API_KEY = "bISrNciS0j0yT4WGEWHnkj6cuhs1eZw6"

    # Endereço que enviaremos os dados
    API_ENDPOINT = "https://pastebin.com/api/api_post.php"

    # Esse e o codigo que queremos enviar
    source_code = texto
    # O "data" tem tudo que
    data = {'api_dev_key': API_KEY,
            'api_option': 'paste',
            'api_paste_code': source_code,
            'api_paste_format': 'json',
            'api_paste_expire_date': '6M'}

    # Post dos nossos dados
    r = requests.post(url=API_ENDPOINT, data=data)
    print(r.content)

import requests

url = 'https://github.com/Borracini/TrabalhoCapturaTratamento'
#tentei somar essa url com o  + '?raw=True' mas não adiantou

mandar_api(url)


'''Tentativa de mandar um json'''
# import json
# with open('data/dict_to_json') as infile:
#     data = json.load(infile)
# mandar_api(data)