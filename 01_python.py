print("hello")

import webbrowser

base_url='https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query='
idols=['아이유','방탄소년단','ITZY']

for name in idols:
    webbrowser.open(base_url+name)
