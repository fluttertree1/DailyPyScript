"""
题目：分数>=90的用A表示，60-89分用B表示，60分以下用C表示（用三元运算符）
"""
score = float(input("请输入分数："))

grade = 'A' if score >= 90 else 'B' if (score >= 60) else 'C'
print(f"分数{score}的成绩是：{grade}")