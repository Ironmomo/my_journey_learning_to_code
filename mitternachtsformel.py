2# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:34:58 2020

@author: andri
"""
import math

a=float(input("Geben Sie A ein: "))
b=float(input("Geben Sie B ein: "))
c=float(input("Geben Sie C ein; "))


diskriminante=b**2-(4*a*c)

if diskriminante > 0:
    diskri=math.sqrt(diskriminante)
    
    lösung1=((b*-1)+diskri)/(2*a)
    lösung2=((b*-1)-diskri)/(2*a)
    print("x1:",lösung1,"x2:",lösung2)
    
if diskriminante==0:
    lösung=(b*-1)/(2*a)

if diskriminante<0:
    print("Keine Lösung")    