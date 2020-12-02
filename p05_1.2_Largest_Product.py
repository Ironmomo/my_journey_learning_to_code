# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:22:14 2020

@author: andri
"""

import random

raster=[]
highest=[0]

for y in range(20):
    line=[]
    for x in range(20):
        num=random.randint(1,99)
        line.append(num)
    
    raster.append(line)
    print(line)
    
x=0
y=0

###horizontal
for char in range(100):
    a=raster[y][x]
    b=raster[y][x+1]
    c=raster[y][x+2]
    d=raster[y][x+3]
    result=a*b*c*d
    if result>highest[0]:
        highest=[]
        highest.append(result)
        highest.append((y,x))
        highest.append((y,x+1))
        highest.append((y,x+2))
        highest.append((y,x+3))
        
    if x<16:        
        x+=4
    else:
        x=0
        y+=1

x=0
y=0
###vertikal
for char in range(100):
    a=raster[y][x]
    b=raster[y+1][x]
    c=raster[y+2][x]
    d=raster[y+3][x]
    result=a*b*c*d
    if result>highest[0]:
        highest=[]
        highest.append(result)
        highest.append((y,x))
        highest.append((y+1,x))
        highest.append((y+2,x))
        highest.append((y+3,x))
    if y<16:        
        y+=4
    else:
        y=0
        x+=1

x=0
y=0
###diagonal1
for char in range(100):
    a=raster[y][x]
    b=raster[y+1][x+1]
    c=raster[y+2][x+2]
    d=raster[y+3][x+3]
    result=a*b*c*d
    if result>highest[0]:
        highest=[]
        highest.append(result)
        highest.append((y,x))
        highest.append((y+1,x+1))
        highest.append((y+2,x+2))
        highest.append((y+3,x+3))
    if x<16:        
        x+=1
    elif x==16 and y<16:
        y+=1

x=19
y=0
###diagonal2
for char in range(100):
    a=raster[y][x]
    b=raster[y+1][x-1]
    c=raster[y+2][x-2]
    d=raster[y+3][x-3]
    result=a*b*c*d
    if result>highest[0]:
        highest=[]
        highest.append(result)
        highest.append((y,x))
        highest.append((y+1,x-1))
        highest.append((y+2,x-2))
        highest.append((y+3,x-3))
    if x>3:        
        x-=1
    elif x==3 and y<16:
        y+=1

print("")
print(highest)
