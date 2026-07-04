import re

# 修饰re.S 匹配换行
pattern = r'\w+'
content = 'http://www.come.COME is the best person ' \
          'he will solve that he arrive problems ' \
          'niha'
result = re.findall(pattern, content, re.S)
print(result)

# re.I 忽略大小写
pattern = r'\w+'
content = 'PYTHON IS A LANGUAGE IN COMPUTER SCIENCE'
result = re.findall(pattern, content, re.I)
print(result)

# re.M 让^$匹配每行首位
pattern = r'^PYTHON.*SCIENCE\s$'
content = 'PYTHON IS A LANGUAGE IN COMPUTER SCIENCE ' \
          'PYTHON sijaidjsakd SCIENCE ' \
          'PYTHON 123456489 SCIENCE '
result = re.findall(pattern, content, re.M)
print(result)