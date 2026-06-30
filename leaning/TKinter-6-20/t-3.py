from tkinter import *

root = Tk()
root.title('最帅人员名单')
root.geometry('600x300+450+350')

inputLabel = Label(root, text='失效饭', bg='lightblue', fg='green', font='微软雅黑 24 normal')
inputLabel.pack(padx=5, pady=10)

# 设置输入框
inputEntry = Entry(root)
inputEntry.pack(padx=5, pady=10)

# 设置按钮
inputButton = Button(text='点击排名', bg='lightyellow', font='微软雅黑 20 normal')
inputButton.pack(padx=5, pady=10)

outputLabel = Label(root, text='失效饭是最帅的!!!', font='隶书 30 normal')
outputLabel.pack(padx=5, pady=10)

root.mainloop()
