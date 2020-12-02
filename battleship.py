# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:28:41 2020

@author: andri
"""


import random

board=[]
for i in range(15):
    row=[]
    for c in range(10):
        row+="O"
    board.append(row)

    
y=random.randint(0,14)
x=random.randint(0,9)
board[y][x]="T"
#print(board) Um Lösung zu sehen und zu testen

def play(board):
    print("   1  2  3  4  5  6  7  8  9  10")
    print("1  0  0  0  0  0  0  0  0  0  0  ")
    print("2  0  0  0  0  0  0  0  0  0  0  ")
    print("3  0  0  0  0  0  0  0  0  0  0  ")
    print("4  0  0  0  0  0  0  0  0  0  0  ")
    print("5  0  0  0  0  0  0  0  0  0  0  ")
    print("6  0  0  0  0  0  0  0  0  0  0  ")
    print("7  0  0  0  0  0  0  0  0  0  0  ")
    print("8  0  0  0  0  0  0  0  0  0  0  ")
    print("9  0  0  0  0  0  0  0  0  0  0  ")
    print("10 0  0  0  0  0  0  0  0  0  0  ")
    print("11 0  0  0  0  0  0  0  0  0  0  ")
    print("12 0  0  0  0  0  0  0  0  0  0  ")
    print("13 0  0  0  0  0  0  0  0  0  0  ")
    print("14 0  0  0  0  0  0  0  0  0  0  ")
    print("15 0  0  0  0  0  0  0  0  0  0  ")
    
    def user_c():
        status=True
        while status == True:
            user_choice=input("Gebe die X und Y koordinate des Feldes an: ")
            print("")
            user_choice=user_choice.split(" ")
            
            if len(user_choice)==2:
                try:                    
                    x,y=user_choice
                    x=int(x)
                    y=int(y)
                except ValueError:
                    print("Geben Sie das korrekte Format ein und Achtung x <=10 und y <=15")

                    
                else:
                    if x<=10 and y<=15:
                        return x,y
            
            else:
                print("Geben Sie das korrekte Format ein und Achtung x <=10 und y <=15")
            

            
    def rounds(board,choice):
        counter=10
        for pick in range(10):
            if board[choice[1]-1][choice[0]-1]=="T":
                print("You win")
                return None
            else:
                board[choice[1]-1][choice[0]-1]="X"
                for i in range(15):
                    linie=""
                    for j in range(10):
                        if board[i][j]=="X":
                            linie+="X "
                        else:
                            linie+="O "
                    print(linie)
                counter-=1
                print("")
                print("Sie haben noch",counter,"versuche")
                choice=user_c()
    
    choice = user_c()      
    rounds(board,choice)
    


play(board)