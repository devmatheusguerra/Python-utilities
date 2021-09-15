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


"""
####################################################################################
#################### Resultado do código acima em 2021-09-15. ######################
####################################################################################

            Date       Open       High        Low      Close  Adj Close      Volume
0     2015-01-02   0.243750   0.243750   0.231562   0.232812   0.215259   6323200.0
1     2015-01-05   0.235625   0.240625   0.229687   0.237187   0.219304  10326400.0
2     2015-01-06   0.238437   0.238437   0.233125   0.234062   0.216414  12572800.0
3     2015-01-07   0.237500   0.242187   0.234687   0.241875   0.223638   6454400.0
4     2015-01-08   0.239375   0.242187   0.237500   0.240000   0.221905   8393600.0
...          ...        ...        ...        ...        ...        ...         ...
1661  2021-09-09  18.900000  19.420000  17.959999  18.850000  18.850000  35169300.0
1662  2021-09-10  19.059999  19.120001  17.180000  17.180000  17.180000  73358000.0
1663  2021-09-13  17.590000  18.040001  17.430000  17.440001  17.440001  35718800.0
1664  2021-09-14  17.540001  17.780001  16.850000  17.030001  17.030001  49175200.0
1665  2021-09-15  17.080000  17.129999  16.490000  16.660000  16.660000  15055100.0

[1666 rows x 7 columns]

"""
