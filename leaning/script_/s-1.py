import requests
# get请求

data = {'name': 'germey',
        'age': 25}
r = requests.get('https://www.baidu.com/index.php?tn=68018901_58_oem_dg', params=data)

print(r.text)


# json格式请求  .json()
r_1 = requests.get('http://httpbin.org/get')
print(type(r_1.text))
print(r_1.json())
print(type(r_1.json()))

# 获取二进制文件
r_2 = requests.get('https://github.com/favicon.ico')
print(r_2.text)  # 字符串类型，解码为字符串
print(r_2.content)  # 字节串类型，原始二进制数据