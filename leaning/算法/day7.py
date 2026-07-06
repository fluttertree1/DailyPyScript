"""
题目：一个5位数，判断是不是回文数，例：12321
"""


def is_five_digit_palindrome(text: str) -> bool:
    return (
        text.isdigit()
        # and len(text) == 5
        and text[0] != '0'
        and text == text[::-1]
    )


if __name__ == "__main__":
    text = input().strip()
    if is_five_digit_palindrome(text):
        print("是回文数")
    else:
        print("不是回文数")


"""
return()的用法，切片
"""