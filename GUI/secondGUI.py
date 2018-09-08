#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'section GUI'

__author__ = "KinSama"

from tkinter import Frame, Tk


class SectionApplication(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        pass


app = SectionApplication()
app.mainloop()

root = Tk()
root.geometry("400x200")
root.mainloop()
