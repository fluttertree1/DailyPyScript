import re

# () 分组
pattern = r'(\w+)'
content = 'PYTHON;123 IS45 A LANGUAGE IN COMPUTER SCIENCE'
result = re.findall(pattern, content)
print(result)

# [] 匹配括号内任意字符
pattern = r'[a-zA-Z]+'
content = 'PYTHON IS A LANGUAGE IN COMPUTER SCIENCE'
result = re.findall(pattern, content)
print(result)

# | 逻辑或
pattern = r'apple|banana|berry'
content = 'I love apple banana berry'
result = re.findall(pattern, content)
print(result)

pattern = r'c(?:at)|b(?:at)'
content = 'cat dog bat'
result = re.findall(pattern, content)
print(result)