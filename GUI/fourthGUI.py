#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'fourth GUI 窗口居中显示'

__author__ = "KinSama"

import tkinter as tk
from tkinter import ttk


def get_screen_size(window):
    '''
    获取屏幕大小
    '''
    return window.winfo_screenwidth(), window.winfo_screenheight()


def get_window_size(window):
    '''
    获取窗口大小
    '''
    return window.winfo_reqwidth(), window.winfo_reqheight()


def center_window(root, width, height):
    '''
    将窗口居中
    '''
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height,
                            (screenwidth - width)/2, (screenheight - height)/2)
    print(size)
    root.geometry(size)


root = tk.Tk()
root.title('测试窗口')
center_window(root, 300, 240)
root.maxsize(300, 240)
root.minsize(300, 240)
ttk.Label(root, relief=tk.FLAT, text='屏幕大小(%sx%s)\n窗口大小(%sx%s)' %
          (get_screen_size(root) + get_window_size(root))).pack(expand=tk.YES)
tk.mainloop()
