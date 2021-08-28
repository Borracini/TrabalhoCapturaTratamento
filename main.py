def save_pickle(ob, name='data/dict_to_pickle'):
    with open(name, 'wb') as handler:
        pickle.dump(ob, handler)
    print('Pickle feito com sucesso!')

def save_json(ob, name='data/dict_to_json'):
    with open(name, 'w') as outfile:  # usar 'w' ou 'wb'?
        json.dump(ob, outfile)
        print('Json feito com sucesso!')

def tamanhos_listas(arquivo):
    with open(arquivo) as infile:
        data = json.load(infile)

    from collections import defaultdict

    tamanhos = defaultdict(list)

    for key in data:
        #tamanhos[key].append(int(len(data[key])))
        if int(key) > 1996:      #professor pediu a partir do ano de 1997
            tamanhos[key] = len(data[key])

    return(tamanhos)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

# -*- coding: utf-8 -*-
    """Exercicio_final.ipynb

    1 - Importe as bibliotecas necessárias requests e BeautifulSoup from bs4

    2 - Utilize a página de referência: 'https://www.google.com/googlebooks/uspto-patents-grants-text.html'
    """

import requests
from bs4 import BeautifulSoup as BS

"""3 - Examine no browser a página de referência
        4 - Utilize a função get da biblioteca requests para capturar os dados da página
        """

url = 'https://www.google.com/googlebooks/uspto-patents-grants-text.html'
resultado = requests.get(url)

"""5 - Utilize a biblioteca BeautifulSoup para interpretar ('parse') o content da página.

    Dica: utilize o intérprete 'html5lib'
    """

interpretacao = BS(resultado.content, "html5lib")

"""6 - Sobre o resultado interpretado (soup) busque por todas (find_all) as seções do tipo a, 
    
    utilizando a opção do atributo href=True: find_all('a', href=True)"""

links1 = interpretacao.find_all('a', href=True)

"""7 - Faça um loop na lista de links encontrada mantendo apenas os links que contém a expressão 'href'
    Dica: use if 'http' in elemento_do_loop
    """

links2 = [l.get('href') for l in links1 if 'http' in l.get('href')]

"""8 - Com outro loop, limpe o resultado para conter apenas os links para os arquivos do tipo *.zip 
    
    que contenham o texto grant_full_text"""

links3 = [elemento for elemento in links2 if 'grant_full_text' in elemento]

"""9 - Há várias maneiras de separar a lista por anos.

      i.Uma possibilidade:

       a.Use: from collections import defaultdict

       b.Crie um dicionário do tipo my_dict = defaultdict(list)

           a.Assim, será possível adicionar elementos em uma lista, para cada ano (chave do dicionário)
           b.Faça um loop que vai de 1976 a 2016
                a. Dentro desse loop, faça outro loop que passa por todos os links da lista
                       a.Teste se o ano está presente no elemento do loop
                              a. Caso verdadeiro, adicione ao seu dicionário, com a chave do ano o elemento
           c.Algo assim (pseudocodigo)
               a.Cria dicionário
               b.Para o ano entre os anos de 1976 a 2015 inclusive,
                  a.Para o link dentro da lista que contém todos os links
                      a.Se o ano estiver contido no link
                          a.Então, adicione ao dicionário, utilizando a chave ano
                          b.my_dic[ano].append(link)
     ii.Imprime o tamanho da lista de cada ano para saber o número de links daquele ano

    """

from collections import defaultdict

my_dict = defaultdict(list)

for ano in range(1976, 2016):
    for item in links3:
        if str(ano) in item:
            my_dict[ano].append(item)



# for key in my_dict:
#     print(f'O ano {key} tem tamanho {len(my_dict[key])}')

"""10 - Salve o dicionário em pickle"""

import os
import pickle

if not os.path.exists('data'):
    os.mkdir('data')

save_pickle(my_dict)

"""11 - Transforme o dicionário em JSON e salve em JSON"""

import json

save_json(my_dict)


#Criação da figura e do relatório

import json
import matplotlib.pyplot as plt
import seaborn as sns


teste = tamanhos_listas('data/dict_to_json')
teste_valores = [i for i in teste.values()]
teste_chaves = [i for i in teste.keys()]
plt.figure(figsize=(10,5))
sns.barplot(x=teste_chaves,y=teste_valores,color='blue')
plt.title('Quantidade de arquivos ZIP por ano')
plt.xticks(rotation=90)
# plt.show()
plt.savefig('data/grafico')
print('Figura salva com sucesso!')


with open("data/Relatorio.txt", "w", encoding='utf8') as text_file:
    text_file.write(f'Quantidade de anos: {len(my_dict)}\n\n')
    total = 0
    for key in my_dict:
        total = total + len(my_dict[key])
    text_file.write(f'O total de arquivos zip contendo os textos das patentes  no período 1997-2015 é {total}.\n\n')

    for key in my_dict:
        text_file.write(f'O ano {key} tem {len(my_dict[key])} arquivos.\n')
    text_file.close()

