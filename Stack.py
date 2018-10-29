#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 06:12:36 2018

@author: kvinay
Implementing a Stck with Arrays
""" 

class stack(object):
    
    def __init__(self, top=0):
        self.list = []
        self.top = top
        
    def push(self, data):
        self.list.append(data)
        self.top += self.top
    
    def pop(self):
        if not self.list:
            return None
        else:
            print(self.list[self.top])
            self.top -= self.top
            
   
    def peek(self):
        if not self.list:
            return None
        else:
            return self.list[self.top]

    def __repr__(self):
        return(str(self.list))
        
# main
s = stack()
s.push(1) 
s.push(2)
s.push(4)
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)