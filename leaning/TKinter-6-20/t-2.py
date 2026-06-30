from tkinter import *

root = Tk()
root.title('最帅人员名单')
root.geometry('600x300+450+350')

# 设置标签
inputLabel = Label(root, text='失效饭', bg='lightblue', fg='green', font='微软雅黑 24 normal')
inputLabel.pack(padx=5, pady=10, fill=X)

# fill填充，要加expand=True
inputLabel = Label(root, text='Python', bg='lightyellow', fg='green', font='微软雅黑 24 normal')
inputLabel.pack(padx=5, pady=10, fill=BOTH, expand=True)
root.mainloop()
