import pandas as pd
from datetime import datetime, timezone
from os import system as cmd
from os import getcwd as dir
from time import time as unix


def obterAcaoBR(acao, start):
    # Transfomando datas para o formato unix
    start_date = start.split('-')
    dt = datetime(int(start_date[0]), int(start_date[1]), int(start_date[2]))
    unix_start = dt.replace(tzinfo=timezone.utc).timestamp()
    # Adicionando .SA às ações brasileiras
    acao = acao + ".SA"
    # Passando os parâmetros a URI.
    link = f'https://query1.finance.yahoo.com/v7/finance/download/{acao}?period1={int(unix_start)}&period2={int(unix())}&interval=1d&events=history&includeAdjustedClose=true'
    # Download dos dados via CURL para temp.csv
    cmd('curl -s "' + link + '" -o' + dir() + '\\temp.csv')
    # Lendo as informações do arquivo baixado e armazenando-os na variável dataFrame
    dataFrame = pd.read_csv('temp.csv')
    # Excluindo o arquivo
    cmd("del temp.csv")
    # Retornando as informações
    return dataFrame


print(obterAcaoBR('MGLU3', '2015-1-1'))
