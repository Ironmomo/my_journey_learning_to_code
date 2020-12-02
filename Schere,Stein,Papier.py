# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:45:37 2020

@author: andri
"""


import random 

print("******************************")
print("let's play Schere Stein Papier")
print("******************************")

figuren=("Schere","Stein","Papier")
spielen="ja"
spieler_punkte=0
computer_punkte=0

while spielen != "nein":

    spieler_auswahl=int(input("Wähle [1]Schere,[2]Stein,[3]Papier: "))
    spieler_figur=figuren[spieler_auswahl-1]
    
    computer_auswahl=random.randint(0, 2)
    computer_figur=figuren[computer_auswahl]
    
    
    if spieler_figur==computer_figur:
        print("Unentschieden. Der Computer wählte",computer_figur)
        spieler_punkte+=1
        computer_punkte+=1
        
    else:
        if spieler_figur=="Schere":
            if computer_figur=="Stein":
                print("Der Computer gewinnt mit",computer_figur)
                computer_punkte+=1
            else:
                print("Du Gewinnst. Der Computer wählte",computer_figur)
                spieler_punkte+=1
            
        if spieler_figur=="Stein":
            if computer_figur=="Schere":
                print("Du Gewinnst. Der Computer wählte",computer_figur)
                spieler_punkte+=1
            else:
                print("Der Computer gewinnt mit",computer_figur)
                computer_punkte+=1
                
        if spieler_figur=="Papier":
            if computer_figur=="Schere":
                print("Der Computer gewinnt mit",computer_figur)
                computer_punkte+=1
            else:
                print("Du Gewinnst. Der Computer wählte",computer_figur)
                spieler_punkte+=1
      
        
    spielen=input("Falls du noch ne Runde spielen willst drück enter sonst nein ")
    
if spieler_punkte==computer_punkte:
    print("Es steht unentschieden mit",spieler_punkte,"zu",computer_punkte)

elif spieler_punkte>computer_punkte:
    print("Du Gewinnst mit",spieler_punkte,"zu",computer_punkte)
    
else:
    print("Der Computer gewinnt mit ", computer_punkte,"zu",spieler_punkte)