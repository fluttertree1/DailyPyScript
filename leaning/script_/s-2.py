import requests
import re

# 抓取网页
r_3 = requests.get('https://staticl.scrape.cuiqingcai.com/')
pattern = re.compile('<h2.*>(.*?)</h2>',re.S)
titles = re.findall(pattern, r_3.text)
print(titles)

r_3 = requests.get('https://github.com/favicon.ico')
with open('favicon.ico', 'wb') as f:
    f.write(r_3.content)
