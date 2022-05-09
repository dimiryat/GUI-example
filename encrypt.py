# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:08:48 2022

@author: DennisLin
"""
import random

class Encrypt:
    def __init__(self, str = None):
        if str == None:
            self.code = [chr(i) for i in range(97,123)]
            random.shuffle(self.code)
        else:
            self.code = list(str)
        self.alph = [chr(i) for i in range(97,123)]
            
    def __str__(self):
        code = "".join(self.code)
        return "Code: " + code
    
    def toEncode(self, str):
        result = ""
        for i in str:
           if i in self.code:
               j = self.alph.index(i)   
               result += self.code[j]
           else:
               result += i
        return result
    
    def toDecode(self, str):
        result = ""
        for i in str:
            if i in self.code:
                j = self.code.index(i)
                result += self.alph[j]
            else:
                result += i
        return result
    
if __name__=="__main__":
    e = Encrypt()
    print()
    print(e.__str__())
    print()
    s1 = "There is no spoon."
    print("Input : " + s1)
    s2 = e.toEncode(s1)
    print("Encode: " + s2)
    s3 = e.toDecode(s2)
    print("Decode: "+ s3)
    # print()