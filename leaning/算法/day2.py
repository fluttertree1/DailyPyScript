"""
题目：编写一个程序，查找此类所有数字，它们可以被7整除
但不能是5的倍数（在2000到3200之间（均包括在内））

"""
ls = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        ls.append(i)

print(ls)

"""
range使用方法
range(start,end,step)
"""