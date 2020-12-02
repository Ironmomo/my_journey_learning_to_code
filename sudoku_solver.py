# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 23:04:04 2020

@author: andri
"""
board=[ [8, 5, 0,  0, 0, 0,  9, 4, 0],
        [0, 4, 0,  0, 0, 2,  1, 0, 0],
        [0, 0, 0,  4, 0, 8,  0, 2, 7],

        [4, 1, 3,  9, 8, 0,  0, 7, 2],
        [0, 2, 0,  1, 0, 4,  0, 8, 0],
        [9, 8, 0,  0, 3, 6,  4, 1, 5],

        [6, 7, 0,  5, 0, 3,  0, 0, 0],
        [0, 0, 8,  7, 0, 0,  0, 5, 0],
        [0, 9, 5,  0, 0, 0,  0, 3, 6]
        ]

def print_board(board):
    for zeile in range(9):
        print("")
        if zeile%3==0 and zeile!=0:
            print(" ______________________________")
            print("")
        for reihe in range(len(board)):
            if reihe%3==0:
                print(" | ",board[zeile][reihe],end=" ")
            elif reihe==8:
                print(board[zeile][reihe]," | ")
            else:
                print(board[zeile][reihe],end=" ")
            
            
    
def check_valid(board,num,zeile,spalte):
    #zeile
    for z in board[zeile]:
        if z==num:
            return False
        
    #spalte
    for z in range(len(board)):
        if num==board[z][spalte]:
            return False
    
    #box
    box_y_start=(zeile//3)*3
    box_x_start=(spalte//3)*3
    
    for z in range(box_y_start,box_y_start +3):
        for s in range(box_x_start,box_x_start +3):
            if num==board[z][s]:
                return False
    return True
    
def check_empty(board):
    for zeile in range(len(board)):
        for spalte in range(len(board[0])):
            if board[zeile][spalte]==0:
                return zeile,spalte
            
    return None,None
    
def solve(board):
    
    zeile,spalte=check_empty(board)
    print(zeile,spalte)
    
    if zeile==None:
        return True
    
    for num in range(1,10):
        
        if check_valid(board,num,zeile,spalte):
            board[zeile][spalte]=num
            print(zeile,spalte,"guess: ",num)
            if solve(board):
                return True
            
        
            
        board[zeile][spalte]=0
    
    return False

print_board(board)
        
solve(board)
  
print_board(board)
