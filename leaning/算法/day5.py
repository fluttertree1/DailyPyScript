"""
求1+2！+3！+...+20!的和
"""
import math


def sum_factorials(n: int) -> int:
    total = 0
    for i in range(n, n+1):
        total += math.factorial(i)  # 利用math库
    return total


if __name__ == '__main__':
    print(sum_factorials(10))

"""
math.factorial 返回阶乘
"""