
"""
输入三个整数x，y，z，从小到大输出
"""
x = int(input())
y = int(input())
z = int(input())

nums = [x, y, z]
nums.sort()
sorted_num = sorted(nums)  # 列表有sort方法，也可以用sorted函数

print(nums)
print(sorted_num[0], sorted_num[1], sorted_num[2])