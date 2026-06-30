from tkinter import *


def rank_handsome_person():
    name = inputVar.get()
    outputVar.set(f"失效饭是最帅的！！！ 比{name}还要帅")


root = Tk()
root.title('最帅人员名单')
root.iconbitmap("favicon.ico")
root.geometry('600x300+450+350')
# 使用Frame将文本，输入，按钮排到一行
topFrame = Frame(root)
inputLabel = Label(topFrame, text='请输入你觉得最帅的人：', bg='lightblue', fg='green', font='微软雅黑 24 normal')
inputLabel.pack(padx=5, pady=10, side=LEFT)

inputVar = StringVar()
inputEntry = Entry(topFrame, textvariable=inputVar)
inputEntry.pack(padx=5, pady=10, side=LEFT)

inputButton = Button(topFrame, text='点击排名', bg='lightyellow', command=rank_handsome_person)
inputButton.pack(padx=5, pady=10, side=LEFT)
topFrame.pack()

outputVar = StringVar()
outputVar.set('请输入姓名')
outputLabel = Label(root, textvariable=outputVar, font='隶书 20 normal')
outputLabel.pack(padx=5, pady=10, fill=BOTH, expand=True)

root.mainloop()
