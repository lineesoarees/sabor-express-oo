import requests
import json

url= 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' #url do endpoint

response = requests.get(url) # importar 'requests' para usar o metodo e passa a url como parametro , o retorno será um status code
print(response)

if response.status_code == 200: # 200 é o status de sucesso
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = [] #cria lista para passar os dados do restaurane somente se ainda ñ estiver cadastrado
        dados_restaurante[nome_do_restaurante].append({"item": item['Item'], #se já existir, insere os dados do json
                                                       "preco": item['price'],
                                                       "descricao": item['description']}) #a segunda palavra corresponde ao json e é case sensitive
else:
    print(f'Erro {response.status_code}')
    
print(dados_restaurante['Pizza Hut'])

for nome_do_restaurante, dados in dados_restaurante.items(): # cria um arquivo json para cada restaurante do endpoint
    nome_do_arquivo = f'{nome_do_restaurante}.json' # nomeando o arquivo que será criado
    with open(nome_do_arquivo, 'w') as arquivo_restaurante: 
        json.dump(dados, arquivo_restaurante, indent=4)