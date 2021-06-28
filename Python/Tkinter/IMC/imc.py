# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:07:00 2021

@author: Usuario
"""

class IMC:
    def __init__(self, h = 0,w = 0):
        self.heigh = h/100.0
        self.weigh = w
    def calcIMC(self):
        if self.heigh != 0:
            IMC = (self.weigh)/float(self.heigh**2)
        else:
            IMC = 0
        return IMC
    
    
    