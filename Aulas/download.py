#Webscrapping
#tabelas


import pandas as pd
import requests

header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' }
 
url=    'https://br.investing.com/equities/brazil'  #url do site que eu quero fazer scrapping

request = requests.get(url, headers=header )

df = pd.read_table(request.text)







