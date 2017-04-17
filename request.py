import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/cinema/nowplaying/guangzhou/'
r = requests.get(url)
r_html = r.text
# 解析 html
soup = BeautifulSoup(r_html, "html.parser")
# 获取 li 标签下的 h2 标签下的 a 标签
mylist = soup.select("li > h2 > a")
# 依次提取 a 标签中包含的文本
result = []
for i in mylist:
    result.append(i.string.extract())
print (result)
