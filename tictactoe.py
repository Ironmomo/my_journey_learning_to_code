# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 18:40:00 2020

@author: andri
"""

#### Dieses Programm ermöglicht zwei Spielern TICTACTOE zu spielen. 
#### Gibt es einen Sieger oder unentschieden, so fragt das Programm erneut, ob es sich starten sollte.
#### Mir war es wichtig, dass das Programm solange läuft wie man spielen möchte und 
#### dass der User-Input keinen Error auslöst.


#### Fragt den aktuellen Spieler nach der Position wo er setzen möchte.
#### Funktion wird erst beendet, wenn der User-Input korrekt ist

def user_input(board):
    while True:
        position = input("Where u want to set your Stone: ")
        try:
            position = int(position)

        except ValueError:
            print("Choose a number 1-9")
            
        else:                     #### Input wird nach den Indexstellen aufgelöst
            position -= 1
            if position in range(9):
                x = position % 3
                y = position // 3
                position = y,x
                if check_pos(position,board):
                    return position
                
            print("Position not valid")
 

#### Überprüft ob die Position bereits besetzt ist
            
def check_pos(position,board):
    if board[position[0]][position[1]] !="X" and board[position[0]][position[1]] !="O":
        return True

#### Setzt den Spielstein auf die gewünschte Position 

def set_board(symbol,position,board):
    board[position[0]][position[1]] = symbol
    return board


#### Überprüft das Spielbrett auf Sieger bzw. ob es voll ist.
        
def check_board(symbol,position,board):
    countx = 0
    county = 0
    countd = 0
    ####horizontal
    for char in board[position[0]]:
        if char == symbol:
            countx += 1 

    ####senkrecht
    for reihe in board:
        if reihe[position[1]] == symbol:
            county += 1
            
    ####diagonal
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        countd = 3
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        countd = 3
        
    ####winner?
    if countx == 3 or county == 3 or countd == 3:
        print("We have a winner {} wins!!".format(symbol))
        return False
    
    ####Sind alle Positionen belegt?
    for y in board:
        for x in y:
            if x in range(10):
                return True
            
    print("The board is full you are equal")
    return False


#### Gibt das Spielbrett in einer koventionellen TicTacToe darstellung aus
       
def print_board(board):
    print("")
    print(" ", board[0][0] , " | ",board[0][1]," | ",board[0][2])
    print("_________________\n")
    print(" ", board[1][0] , " | ",board[1][1]," | ",board[1][2])
    print("_________________\n")
    print(" ", board[2][0] , " | ",board[2][1]," | ",board[2][2])


#### Koordienert die Funktionen und den Spielablauf
    
def main():
    
    run = True
    while run:  #### Läuft solange der Benutzer Spielen möchte und setzt das Spielbrett zurück
        
        board = [[1,2,3],
             [4,5,6],
             [7,8,9]
             ]
        play = True
        active_player = 1
        
        while play:  #### Struktur der einzelnen Runden. Läuft solange kein Gewinner bzw. Board voll
    
            if active_player == 1:
                symbol = "X"
            else:
                symbol = "O"
                
            print_board(board)
            position = user_input(board)
            board = set_board(symbol, position, board)
            play = check_board(symbol, position, board)
            
                    
            
            if active_player == 1:
                active_player = -1
                
            else:
                active_player = 1
                
            
        again = input("Enter 'y' for another round: ")
        
        if again != "y":
            run = False
        
        
            
main()
            
            
            
            
            
            
        
        
                   