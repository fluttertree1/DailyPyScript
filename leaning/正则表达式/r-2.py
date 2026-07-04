import re
# ^ 匹配字符串开头
pattern = r'^name\s\w+'
contents = [
    'name this is a test',
    'name nihao',
    'hel this re using',
    'COME is a handsome man'
]
for content in contents:
    result = re.match(pattern, content)
    if result:
        print(result.group())
    else:
        print("没有匹配成功")

# & 匹配字符串末尾
pattern = r'come$'
content = 'http.come'
result = re.search(pattern, content)
if result:
    print(result.group())
else:
    print("没有匹配成功")