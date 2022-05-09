# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:53:00 2022

@author: DennisLin
"""

from tkinter import *
from tkinter.ttk import *

class EncryptView(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.winfo_toplevel().title("Encryption tool")
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.it = Label(self)
        self.it["text"] = "Input:"
        self.it.grid(row=0, column=0, sticky=N+E)
        
        self.ifd = Entry(self)
        self.ifd["width"] = 60
        self.ifd.grid(row=0, column=1, columnspan=6, sticky=N+W)
        
        self.ot = Label(self)
        self.ot["text"] = "Output:"
        self.ot.grid(row=1, column=0, sticky=N+E)
        
        self.ofd = Entry(self)
        self.ofd["width"] = 60
        self.ofd.grid(row=1, column=1, columnspan=6, sticky=N+W)
        
        self.nb = Button(self)
        self.nb["text"] = "New"
        self.nb.grid(row=2, column=0, stick=N+W)
        
        self.lb = Button(self)
        self.lb["text"] = "Load"
        self.lb.grid(row=2, column=1, sticky=N+W)
        
        self.sb = Button(self)
        self.sb["text"] = "Save"
        self.sb.grid(row=2, column=2, sticky=N+W)
        
        self.eb = Button(self)
        self.eb["text"] = "Encode"
        self.eb.grid(row=2, column=3, sticky=N+W)
        
        self.db = Button(self)
        self.db["text"] = "Decode"
        self.db.grid(row=2, column=4, sticky=N+W)
        
        self.cb = Button(self)
        self.cb["text"] = "Clear"
        self.cb.grid(row=2, column=5, sticky=N+W)
        
        self.cb2 = Button(self)
        self.cb2["text"] = "Copy"
        self.cb2.grid(row=2, column=6, sticky=N+W)
        
        self.dt = Label(self)
        m = "Message"
        self.dt["text"] = m
        self.dt.grid(row=3, column=0, columnspan=7, sticky=N)
        
if __name__ == '__main__':
    root = Tk()
    app = EncryptView(master=root)
    root.mainloop()