from tkinter import *

root = Tk()
root.title('最帅人员名单')
root.geometry('600x300+450+350')
# 使用Frame将文本，输入，按钮排到一行
topFrame = Frame(root)
inputLabel = Label(topFrame, text='失效饭', bg='lightblue', fg='green', font='微软雅黑 24 normal')
inputLabel.pack(padx=5, pady=10, side=LEFT)

inputEntry = Entry(topFrame)
inputEntry.pack(padx=5, pady=10, side=LEFT)

inputButton = Button(topFrame, text='点击排名', bg='lightyellow')
inputButton.pack(padx=5, pady=10, side=LEFT)
topFrame.pack()

outputLabel = Label(root, text='失效饭是最帅的!!!', font='隶书 30 normal')
outputLabel.pack(padx=5, pady=10)

root.mainloop()
