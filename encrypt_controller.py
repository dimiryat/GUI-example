# -*- coding: utf-8 -*-
"""
Created on Wed May  4 13:46:23 2022

@author: DennisLin
"""

from tkinter import Tk
from encrypt_view import EncryptView
from encrypt import Encrypt
import os

class EncryptController:
    def __init__(self):
        self.app = EncryptView(master=Tk())
        self.app.nb["command"] = self.nm
        self.app.lb["command"] = self.lm
        self.app.sb["command"] = self.sm
        self.app.eb["command"] = self.em
        self.app.db["command"] = self.dm
        self.app.cb["command"] = self.cm
        self.app.cb2["command"] = self.cm2
        self.app.mainloop()
        
        self.e = None
        self.userinput = ""
        self.result = ""
        
    def nm(self):
        self.e = Encrypt()
        self.app.dt["text"] = self.e
        
    def lm(self):
        if os.path.exists(".\code.txt"):
            f = open('.\code.txt', 'r')
            code = f.readline()
            self.e = Encrypt(code)
            s = str("".join(self.e.code))
            m = "Code: " + s
            self.app.dt["text"] = m
        else:
            m = "Load can't be done for now!"
            self.app.dt["text"] = m
        
    def sm(self):
        if self.e == None:
            m = "Save can't be done for now!"
            self.app.dt["text"] = m
        else:
            f = open('.\code.txt', 'w')
            f.write("".join(self.e.code))
            f.closed
            self.app.dt["text"] = "Save completed"
        
    def em(self):
        self.userinput = self.app.ifd.get()
        if self.userinput == "":
            m = "No input!"
            self.app.dt["text"] = m
        else:
            if self.e == None:
                m = "No code table!"
                self.app.dt["text"] = m
            else:
                s = self.userinput
                r = self.e.toEncode(s)
                self.result = r
                self.app.ofd.delete(0, 200)
                self.app.ofd.insert(0, r)
                m = "Encoding completed!"
                self.app.dt["text"] = m
    
    def dm(self):
        self.userinput = self.app.ifd.get()
        if self.userinput == "":
            m = "No input!"
            self.app.dt["text"] = m
        else:
            if self.e == None:
                m = "No code table!"
                self.app.dt["text"] = m
            else:
                s = self.userinput
                r = self.e.toDecode(s)
                self.result = r
                self.app.ofd.delete(0, 200)
                self.app.ofd.insert(0, r)
                m = "Decoding completed!"
                self.app.dt["text"] = m
        
    def cm(self):
        self.e = None
        self.userinput = ""
        self.result = ""
        self.app.ifd.delete(0, 200)
        self.app.ofd.delete(0, 200)
        self.app.dt["text"] = "Cleared!"
        
    def cm2(self):
        if self.result == "":
            m = "Copying can't be done for now"
            self.app.dt["text"] = m
        else:
            self.app.clipboard_clear()
            r = self.result
            self.app.clipboard_append(r)
            m = "Copying completed!"
            self.app.dt["text"] = m
        
if __name__ == '__main__':
    app = EncryptController()