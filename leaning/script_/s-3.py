import requests
import re

# 正则表达式
# ^匹配字符串的开头
# \s 匹配空白字符
# \d 匹配数字
# \w 匹配字母
# .*万能匹配符（贪婪）
# .*?(非贪婪）
# 修饰符 re.S（包括换行符在内的所有字符）re.l(对大小写不敏感) re.X...re.M(多行匹配)

message = '123456'
result = re.match(r'\d+', message)
print(result.group())
# match方法
content = "Hellos 123 4567 World_This is a Regex Demo"

result = re.match(r'^Hello\w\s\d\d\d', content)
print(result.group())
