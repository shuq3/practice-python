import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/cinema/nowplaying/guangzhou/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")
mylist = soup.select("li > h2 > a")
result = []
for i in mylist:
    result.append(i.string.extract())
print (result)
