import re

# 基本字符 +多个字符，
# \d 匹配数字
pattern = r'\d+'
content = '123456'
result = re.match(pattern, content)
print(result.group())

# \w 匹配字母,数字，下划线
pattern = r'\w+'
content = 'test'
result = re.match(pattern, content)
print(result.group())

# \s 匹配空格
pattern = r'\w+\s\w+\s\w+\s\w+'
content = 'This is a test content'
result = re.match(pattern, content)
print(result.group())

# \b 匹配单词边界
pattern = r'\bHello\b\s'
content = 'Hello world this is a test'
result = re.match(pattern, content)
print(result.group())

# ^ 匹配字符串开头
pattern = r'^name\s\w+\s\w+'
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
pattern = r'^http\w'
content = 'http://localhost/come'
result = re.match(pattern, content)
if result:
    print(result.group())
else:
    print("没有匹配成功")