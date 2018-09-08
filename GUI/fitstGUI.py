#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'fitst GUI'

__author__ = "KinSama"

from tkinter import Frame, Entry, Button
import tkinter.messagebox as messagebox


# 在GUI中，每个Button、Label、输入框等，都是一个Widget。
# Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
# pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。

class FirstApplication(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.quitButton = Button(self, text="hello", command=self.hello)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'word'
        messagebox.showinfo('Message', 'hello,%s' % name)


app = FirstApplication()
app.master.title("H ")
app.mainloop()
