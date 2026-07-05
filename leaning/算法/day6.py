"""
利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
"""

# 利用后进先出的原理
# 0， 1， 2， 3， 4
# 4， 3， 2， 1， 0
def print_reverse(chars, idx=0):
    if idx >= len(chars):
        return
    print_reverse(chars, idx + 1)

    print(chars[idx], end='')


if __name__ == "__main__":
    data = input()
    print_reverse(data)