import re

# 量词

# * (0次+)
pattern = r'.*'
content = 'PYTHON IS A LANGUAGE IN COMPUTER SCIENCE'
result = re.findall(pattern, content)
print(result)

# + 一次以上
pattern = r'[a-zA-Z]+'
content = '123456 a123 abcd'
result = re.findall(pattern, content)
print(result)

#  ? 0或1次
pattern = r'[0-9]'
content = '1 0 a bc'
result = re.findall(pattern, content)
print(result)

# {m,n} m到n次
pattern = r'\d{5}'
content = '12345 12345678'
result = re.findall(pattern, content)
print(result)