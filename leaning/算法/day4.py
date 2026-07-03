gi"""
统计字符串中的英文，数字，和空格
"""
string = input()
count_w = sum(1 for n in string if n.isalpha())
count_s = sum(1 for n in string if n.isspace())
count_n = sum(1 for n in string if n.isdigit())
count_l = len(string) - count_w - count_s - count_n

print(f"字母：{count_w},空格：{count_s},数字：{count_n},其他:{count_l}")

"""
列表推导式生成的是一个迭代器对象，使用print打印出来的是地址
"""