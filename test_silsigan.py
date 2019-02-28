import requests
from bs4 import BeautifulSoup

url='https://www.naver.com'

# 1. python requesets를 통해 요청보내기

response=requests.get(url).text
#print(response)

# 2. 크롬 브라우저로 보는것을 대신해서,
#  문자열을 DOM구조(html)로 변환한다
soup=BeautifulSoup(response,'html.parser')
# 3. 선택자를 활용해서 내가 원하는 값을 가져온다.

#이거로 해도되고 아래거로 해도됨
#silsigan=soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul')
silsigan=soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base .ah_k')

#print(silsigan[0].text)

for idx,i in enumerate(silsigan): #list를 숫자랑 같이 쓰고싶을때 보통 사용하는 열거형
    print(idx+1,i.text)

#print(kospi)
