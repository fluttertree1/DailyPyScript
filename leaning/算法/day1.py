"""题目：有1,2,3,4个数字能组成多少个互不相同且无重复数字的三位数？都是多少？
digits = [1, 2, 3, 4]
"""

digits = [1, 2, 3, 4]
nums = []
for a in digits:
    for b in digits:
        if a == b:
            continue
        for c in digits:
            if a == c or b == c:
                continue
            nums.append(a*100+b*10+c)

print(nums)
print(f"一共有{len(nums)}种组合")


"""
用for循环实现全组合，再去除不符合条件的组合。

若从正面直接列出题目要求的组合比较困难，所以从反向实现
continue实现跳出循环
"""