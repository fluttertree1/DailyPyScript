from tkinter import *


def tax_calculate():
    inputMoney = inputVar.get()
    if inputMoney.isdigit():
        output = int(inputMoney)*0.2  # 省略计算过程
        outputVar.set(f"个人所得税：{output:.2f}")
        print(f"个人所得税：{output:.2f}")
    else:
        outputVar.set("请输入整数")
        print("请输入整数")


# 创建窗口
root = Tk()
root.title('个人所得税计算器 1.0')
root.iconbitmap("favicon.ico")
root.geometry('600x300+450+350')

# 使用Frame将文本，输入，按钮排到一行
topFrame = Frame(root)
inputLabel = Label(topFrame, text='请输入工资：', fg='purple', bg='lightblue', font='微软雅黑 10 normal')
inputLabel.pack(padx=5, pady=10, side=LEFT, fill=BOTH)

# 设置输入框
inputVar = StringVar()
inputEntry = Entry(topFrame, textvariable=inputVar)
inputEntry.pack(padx=5, pady=10, side=LEFT)

# 设置按钮
inputButton = Button(topFrame, text='计算', bg='lightyellow', command=tax_calculate)
inputButton.pack(padx=5, pady=10, side=LEFT)
topFrame.pack(padx=5, pady=5)

# 设置输出结果
outputVar = StringVar()
outputVar.set('点击计算')
outputLabel = Label(root, textvariable=outputVar, font='隶书 30 normal', fg='green', bg='lightblue')
outputLabel.pack(padx=5, pady=10, fill=BOTH, expand=True)

root.mainloop()
