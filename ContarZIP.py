import json
with open('data/dict_to_json') as infile:
    data = json.load(infile)

import urllib.request
from collections import defaultdict

output_size = defaultdict(int)

for key,value in data.items():
    for i in range(0, len(data[key])):
        link = data[key][i]
        # output_size[key] = 0
        with urllib.request.urlopen(link) as handler:
            # print(f'O ano é {key} e o índice é {i}\n')
            # a = int(handler.getheader('Content-Length'))
            # print(f'O tamanho é {a}\n')
            output_size[key] += int(handler.getheader('Content-Length'))
            # print(f'O tamanho total é {output_size[key]} para o ano de {key}\n')


def save_json(ob, name='data/somas_tamanhos'):
    with open(name, 'w') as outfile:  # usar 'w' ou 'wb'?
        json.dump(ob, outfile)
        print('Json feito com sucesso!')

save_json(output_size)