import threading
import time
import requests
import re
from pyquery import PyQuery as pq
'''线程（主线程和子线程）
def target(second):
    print(f'Threading {threading.current_thread().name} is running')
    print(f'Threading {threading.current_thread().name} sleep {second}s')
    time.sleep(second)
    print(f'Threading {threading.current_thread().name} is ended')

print(f'Threading {threading.current_thread().name} is running')
for i in [1,5]:
    t = threading.Thread(target=target,args=[i])
    t.start()
print(f'Threading {threading.current_thread().name} is ended')
'''
            # get请求
# data = {'name':'germey',
#         'age': 25}
# r = requests.get('https://www.baidu.com/index.php?tn=68018901_58_oem_dg',params=data)
# print(r.text)


            #json格式请求  .json()
# r_1 = requests.get('http://httpbin.org/get')
# print(type(r_1.text))
# print(r_1.json())
# print(type(r_1.json()))
            # 获取二进制文件
r_2 = requests.get('https://github.com/favicon.ico')
print(r_2.text)  # 字符串类型，解码为字符串
print(r_2.content)  # 字节串类型，原始二进制数据
# 抓取网页
# r_3 = requests.get('https://staticl.scrape.cuiqingcai.com/')
# pattern = re.compile('<h2.*>(.*?)</h2>',re.S)
# titles = re.findall(pattern,r_3.text)
# print(titles)
#
# r_3 = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico', 'wb') as f:
#     f.write(r_3.content)

            # 正则表达式
# ^匹配字符串的开头
# \s 匹配空白字符
# \d 匹配数字
# \w 匹配字母
# .*万能匹配符（贪婪）
# .*?(非贪婪）
# 修饰符 re.S（包括换行符在内的所有字符）re.l(对大小写不敏感) re.X...re.M(多行匹配)
#   result = re.match('He.*?(\d+).*?Dome$',content,re.S)
            # match方法 从字符串的起始位置匹配正则表达式，必须与开头匹配
#           group()可以输出匹配内容
#           span可以输出匹配的范围
# content = 'Hellos 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
# print(result)

            # 在一段文本中提取邮件或电话号码可以用（）将想提取的子字符串括起来
            # 每个（）对应一个分组，调用group传入分组的索引可以获取提取的结果
# content = 'Hellos 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld',content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())


# content = 'Hellos 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^He.*?(\d+).*Demo$',content)
# print(result)
# print(result.group(1))
# 如果字符串有.就用转义匹配
# content = '(百度）www.baidu.com'
# result = re.match('\(百度\)www.\baidu\.com',content)
            #search方法，匹配时会扫描整个字符串，然后返回第一个成功匹配的结果，
            # 依次扫描字符串，直到第一个符合规则的字符串（任意位置）
# result = re.search('<li.?*active.*?singer="(.*?)">(>*?)<\a>', html, re.S)
# if result:
#     print(result.group(1),result.group(2))



# 优化建议，先用match，再用search

# if not re.match(r"http://", url):  # 快速失败
#     if re.search(r"\.jpg$", url):   # 二次检查
#         process_image(url)

            # finall方法，搜索整个字符串，返回匹配的所有内容
            # s = re.finall(正则，文本，修饰符)
            # sub方法，把文本中的所有数字（其他）去掉
            # c = re.sub('\d+','',c)
            # compile方法，将正则字符串编译成正则表达式对象，可以复用
            # pattern = re.compile('\d{2}:\d{2})
            # r1 = re.sub(pattern,''',c1)

            #PyQuery
# doc = pq(url='https://cuiqingcai.com')
# print(doc('title'))