#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'作为工具的入口'

__author__ = "KinSama"

from tkinter import *
from tkinter.filedialog import askdirectory


class LittleTool(Frame):
    '''
    小工具
    '''

    def __init__(self, master=None):
       # Frame似乎只是一个面板
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        '''
        创建ui内容
        '''
        # 邮箱账号
        self.emailLbl = Label(self, text="邮箱账号：")
        self.emailLbl.grid(row=0, column=0, sticky=W)
        self.emailInput = Entry(self)
        self.emailInput.grid(row=0, column=1)
        # 邮箱授权码
        self.passwordLbl = Label(self, text="授权码：")
        self.passwordLbl.grid(row=1, column=0, sticky=W)
        self.passwordInput = Entry(self)
        self.passwordInput.grid(row=1, column=1)
        # pop服务器
        self.serverLbl = Label(self, text="POP3服务器：")
        self.serverLbl.grid(row=2, column=0, sticky=W)
        self.serverInput = Entry(self)
        self.serverInput.grid(row=2, column=1)
        # 保存附件的文件夹
        self.attaLbl = Label(self, text="接收附件：")
        self.attaLbl.grid(row=3, column=0, sticky=W)
        self.path = StringVar()
        self.attaInput = Entry(self, textvariable=self.path, state=DISABLED)
        self.attaInput.grid(row=3, column=1)
        self.attaBtn = Button(self, text="选择文件夹", command=self.selectPath)
        self.attaBtn.grid(row=3, column=2)
        # 确认
        self.submitBtn = Button(self, text="确定", width=10)
        self.submitBtn.grid(row=4, column=1)

    def selectPath(self):
        self.path.set(askdirectory())


root = Tk()
root.title("批量接收邮件附件")
little = LittleTool(root)
# 获取屏幕宽高
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
width = 350  # root.winfo_reqwidth()
height = 130  # root.winfo_reqheight()
# 设定窗口位置及大小
size = '%dx%d+%d+%d' % (width, height,
                        (screenwidth - width)/2, (screenheight - height)/2)
root.geometry(size)
# 使窗口无法放大缩小
root.resizable(width=False, height=False)
root.mainloop()
