import requests
from bs4 import BeautifulSoup

url='http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum'

name=[]
s=[]
# 1. python requesets를 통해 요청보내기

response=requests.get(url).text
#print(response)

# 2. 크롬 브라우저로 보는것을 대신해서,
#  문자열을 DOM구조(html)로 변환한다
soup=BeautifulSoup(response,'html.parser')
# 3. 선택자를 활용해서 내가 원하는 값을 가져온다.
kospi=soup.select('.link')

for country in kospi:
    print(country.select_one('.name').text)
    print(country.select_one('.idx').text)
#print(sale)
#for i,j in zip(name, s):
#    print(i,j)

