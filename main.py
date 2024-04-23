import yfinance as yf
import pandas as pd

import warnings

warnings.simplefilter("ignore")

# IBOV

ibov = yf.Ticker('^BVSP')

historic_ibov = ibov.history(start='2003-09-16', end='2023-09-16')['Close']

print(historic_ibov)

# IMA-B

imab = pd.read_excel('data/imab-historico.xls', engine='openpyxl')

filter_imab = imab.loc[imab['Data de Referência'] < '2023-09-16', ['Data de Referência', 'Número Índice']]
    
historic_imab = filter_imab.set_index('Data de Referência')

print(historic_imab)

# CDI

result = pd.concat([historic_ibov, historic_imab], axis=1)

print(result)