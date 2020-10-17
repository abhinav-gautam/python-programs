# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:08:44 2019

@author: abhinav
"""

def pyramid_pat(n):
    for i in range(n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
pyramid_pat(5)     

def reverse_pyramid(n):
    k=2*n-2
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k-=2
        for j in range(i+1):
            print("* ",end="")
        print("\r")
reverse_pyramid(5)

def triangle(n):
    k=2*n-2
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k-=1
        for j in range(i+1):
            print("* ",end="")
        print("\r")
triangle(5)

def number_pat(n):
    num = 1
    for i in range(n):
        num=1
        for j in range(i+1):
            print (num,end=" ")
            num+=1
        print("\r")
number_pat(5)

def number_pat2(n):
    num = 1
    for i in range(n):
        for j in range(i+1):
            print (num,end=" ")
            num+=1
        print("\r")
number_pat2(5)
            
def character_pat(n):
    num=65
    for i in range(n):
        num = 65
        for j in range(i+1):
            print(chr(num),end=" ")
            num+=1
        print("\r")
character_pat(5)

def square_triangle(n):
    k=2*n
    num=1
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k-=2
        for j in range(i+1):
            print(num**2,end=" ")
            num+=1
        print("\r")
square_triangle(5)
            
        