import re

# match方法，从字符串开头查找,不匹配则返回None
pattern = r'come$'
content = 'http://www.come'
result = re.match(pattern, content)
if result:
    print(result.group())
else:
    print("没有匹配成功")

# search方法,从整个字符串查询
pattern = r'come$'
content = 'http://www.come'
result = re.search(pattern, content)
if result:
    print(result.group())
else:
    print("没有匹配成功")

# findall 返回所有匹配的字符串列表
pattern = r'\w+'
content = 'This is findall list test'
result = re.findall(pattern, content)
if result:
    print(result)
else:
    print("没有匹配成功")

# findall捕获组  每个元素是元组
pattern = r'(\d+)(\w+)'
content = '123abc-456efg-789hij'
result = re.findall(pattern, content)
if result:
    print(result)
else:
    print("没有匹配成功")


# sub 替换
