import requests
from bs4 import BeautifulSoup
import pandas as pd
from pymongo import MongoClient

client=MongoClient()
col=client['test']['test']
url='https://worldpopulationreview.com/country-rankings/olympic-medals-by-country'
r=requests.get(url)

soup=BeautifulSoup(r.text,'html.parser')

table=soup.find('tbody')


A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in table.findAll('tr'):
    cells=row.findAll('td')
    A.append(cells[0].text)
    B.append(cells[1].text)
    C.append(cells[2].text)
    D.append(cells[3].text)
    E.append(cells[4].text)
    F.append(cells[5].text)
df=pd.DataFrame(A,columns=['Country'])
df['Gold']=B
df['Silver']=C
df['Bronze']=D
df['Total Medals']=E
df['2021 Population']=F
print(df)

data=df.to_dict(orient='records')
col.insert_many(data)
