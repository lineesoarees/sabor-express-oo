from fastapi import FastAPI, Query
import requests

app= FastAPI()

@app.get('/api/hello')
def helloWorld():
    return{'Hello':'World'}

@app.get('/api/restaurantes/')
def get_gestaurantes(restaurante: str = Query(None)):
    url= 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' #url do endpoint
    response = requests.get(url) # importar 'requests' para usar o metodo e passa a url como parametro , o retorno será um status code 
    if response.status_code == 200: # 200 é o status de sucesso
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:           
                dados_restaurante.append({"item": item['Item'], #se já existir, insere os dados do json
                                                       "preco": item['price'],
                                                       "descricao": item['description']}) #a segunda palavra corresponde ao json e é case sensitive
        return {'Restaurante': restaurante, 'Itens':dados_restaurante}
    else:
        return{f'Erro {response.status_code} - {response.text}'}