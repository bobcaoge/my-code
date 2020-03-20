# /usr/bin/python3.6
# -*- coding: utf-8 -*-
from tkinter import *

master =Tk()


def callback():
    print('click!')


# 最普通的返回操作，按钮返回一个值（通过一个函数传递）
# b=Button(master,text='OK',command=callback)

# DISABLED  state状态    表示不能按下这个按钮，无法操作这个按钮
# b = Button(master, text="Help", state=DISABLED)

# 当你不设置大小的时候，按钮能容纳所有东西；当然你也可以指定大小：padx，pady
# b = Button(master, text="Help", state=DISABLED, padx=59, pady=99)

# 当然我们也可以在按钮里面在写入一个窗体，窗体一般是用像素来表示的，所以按钮也是可以按照像素来进行表示的，位图也是可以的
f = Frame(master, height=320, width=320)
f.pack_propagate(0) # don't shrink
f.pack()
b = Button(f, text="Sure!")#将窗体导入
# b.pack(fill=BOTH, expand=1)#填充顶部，扩展

# 当text有多行的时候
# b = Button(master, text='longtext阿士大夫撒旦法士大夫撒旦法longtext阿士大夫撒旦法士大夫撒旦法longtext阿士大夫撒旦法士大夫撒旦法', anchor=W, justify=LEFT, padx=2)

# 这个操作是让按钮好像已经按下去了但是实际上没有触发按钮的功能，再点击就能触发
# b.config(relief=SUNKEN)

# b = Checkbutton(master, image=, variable='var', indicatoron=0)
# b = Button(master, text="Click me", image='pattern', compound=CENTER)


b.pack()

mainloop()

