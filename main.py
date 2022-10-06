import config
import requests

from datetime import datetime
from modelo.cotacao import Cotacao



URL_BASE = f'https://hgbrasil.com/status/finance?key={config.api_key}'

 def consultar_dados_financeiros() -> Cotacao:
    requisicao = requests.get(URL_BASE)
    dados = requisicao.json()['results']['currencies']

    dolar = float(dados['USD']['buy'])
    euro = float(dados['EUR']['buy'])
    data_hora = str(datetime.now)
    return Cotacao (dolar=dolar, euro=euro, data_hora=data_hora)



if __name__=='__main__':
    consultar_dados_financeiros()

