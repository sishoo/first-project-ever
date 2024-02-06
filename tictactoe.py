alreadyTaken = False
alreadyTaken1 = False
alreadyTaken2 = False
alreadyTaken3 = False
alreadyTaken4 = False
alreadyTaken5 = False
alreadyTaken6 = False
alreadyTaken7 = False
alreadyTaken8 = False
q1 = 10
q2 = 10
q3 = 10
q4 = 10
q5 = 10
q6 = 10
q7 = 10
q8 = 10
q9 = 10
youWinVariable = False


XO = "X"




def game():
    Line(133, 0, 133, 400)
    Line(266, 0, 266, 400)
    Line(0, 133, 400, 133)
    Line(0, 266, 400, 266)

def onMousePress(mouseX, mouseY):
    global youWinVariable
    global alreadyTaken
    global XO
    global alreadyTaken1
    global alreadyTaken2
    global alreadyTaken3
    global alreadyTaken4
    global alreadyTaken5
    global alreadyTaken6
    global alreadyTaken7
    global alreadyTaken8
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9

    if youWinVariable == False:
        if mouseX in range(0, 133) and mouseY in range(0, 133):
            if alreadyTaken == False:
                Label(XO, 60, 60, size=100)
                alreadyTaken = True
                if XO == "X":
                    q1 = 1
                    XO = "O"
                    print("O's turn")
                elif XO == "O":
                    q1 = 2
                    XO = "X"
                    print("X's turn")
                checkWin()
            
            
            
                
        elif mouseX in range(133, 266) and mouseY in range(0, 133):
            if alreadyTaken1 == False:
                Label(XO, 200, 60, size=100)
                alreadyTaken1 = True
                if XO == "X":
                    q2 = 1
                    XO = "O"
                    print("O's turn")
                elif XO == "O":
                    q2 = 2
                    XO = "X"
                    print("X's turn")
                checkWin()
            
            
            
            
        elif mouseX in range(266, 400) and mouseY in range(0, 133):
            if alreadyTaken2 == False:
                Label(XO, 330, 60, size=100)
                alreadyTaken2 = True
                if XO == "X":
                    q3 = 1
                    XO = "O"
                    print("O's turn")
                elif XO == "O":
                    q3 = 2
                    XO = "X"
                    print("X's turn")
                checkWin()
        
        
        
        elif mouseX in range(0, 133) and mouseY in range(133, 266):
            if alreadyTaken3 == False:
                Label(XO, 60, 195, size=100)
                alreadyTaken3 = True
                if XO == "X":
                    q4 = 1
                    XO = "O"
                    print("O's turn")
                elif XO == "O":
                    q4 = 2
                    XO = "X"
                    print("X's turn")
                checkWin()
                
                
                
        elif mouseX in range(133, 266) and mouseY in range(133, 266):
            if alreadyTaken4 == False:
                Label(XO, 200, 195, size=100)
                alreadyTaken4 = True
                if XO == "X":
                    q5 = 1
                    XO = "O"
                    print("O's turn")
                elif XO == "O":
                    q5 = 2
                    XO = "X"
                    print("X's turn")
                checkWin()
              
              
        elif mouseX in range(266, 400) and mouseY in range(133, 266):
            if alreadyTaken5 == False:
                Label(XO, 330, 195, size=100)
                alreadyTaken5 = True
                if XO == "X":
                    q6 = 1
                    XO = "O"
                    print("O's turn")
                elif XO == "O":
                    q6 = 2
                    XO = "X"
                    print("X's turn")
                checkWin()
                
                
        elif mouseX in range(0, 133) and mouseY in range(266, 400):
            if alreadyTaken6 == False:
                Label(XO, 60, 330, size=100)
                alreadyTaken6 = True
                if XO == "X":
                    q7 = 1
                    XO = "O"
                    print("O's turn")
                elif XO == "O":
                    q7 = 2
                    XO = "X"
                    print("X's turn")
                checkWin()
                    
                    
                
        elif mouseX in range(133, 266) and mouseY in range(266, 400):
            if alreadyTaken7 == False:
                Label(XO, 200, 330, size=100)
                alreadyTaken7 = True
                if XO == "X":
                    q8 = 1
                    XO = "O"
                    print("O's turn")
                elif XO == "O":
                    q8 = 2
                    XO = "X"
                    print("X's turn")
                checkWin() 
                    
                    
                
        elif mouseX in range (266, 400) and mouseY in range(266, 400):
            if alreadyTaken8 == False:
                Label(XO, 330, 330, size=100)
                alreadyTaken8 = True
                if XO == "X":
                    q9 = 1
                    XO = "O"
                    print("O's turn")
                elif XO == "O":
                    q9 = 2
                    XO = "X"
                    print("X's turn")
                checkWin()
                
                
    elif youWinVariable == True:
        if mouseX in range(100, 300) and mouseY in range(260, 360):
            playAgain()
    


def checkWin():
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global alreadyTaken1
    global alreadyTaken2
    global alreadyTaken3
    global alreadyTaken4
    global alreadyTaken5
    global alreadyTaken6
    global alreadyTaken7
    global alreadyTaken8
    
    
    
    
    if q1+q2+q3 == 3:
        Line(0, 50, 400, 50, fill="red", lineWidth=10)
        youWin("X")
    elif q1+q2+q3 == 6:
        Line(0, 50, 400, 50, fill="red", lineWidth=10)
        youWin("O")
    elif q1+q4+q7 == 3:
        Line(50, 0, 50, 400, fill="red", lineWidth=10)
        youWin("X")
    elif q1+q4+q7 == 6:
        Line(50, 0, 50, 400, fill="red", lineWidth=10)
        youWin("O")
    elif q1+q5+q9 == 3:
        Line(0, 0, 400, 400, fill="red", lineWidth=10)
        youWin("X")
    elif q1+q5+q9 == 6:
        Line(0, 0, 400, 400, fill="red", lineWidth=10)
        youWin("O")
    elif q2+q5+q8 == 3:
        Line(200, 0, 200, 400, fill="red", lineWidth=10)
        youWin("X")
    elif q2+q5+q8 == 6:
        Line(200, 0, 200, 400, fill="red", lineWidth=10)
        youWin("O")
    elif q3+q6+q9 == 3:
        Line(350, 0, 350, 400, fill="red", lineWidth=10)
        youWin("X")
    elif q3+q6+q9 == 6:
        Line(350, 0, 350, 400, fill="red", lineWidth=10)
        youWin("O")
    elif q4+q5+q6 == 3:
        Line(0, 190, 400, 190, fill="red", lineWidth=10)
        youWin('X')
    elif q4+q5+q6 == 6:
        Line(0, 190, 400, 190, fill="red", lineWidth=10)
        youWin('O')
    elif q7+q8+q9 == 3:
        Line(0, 320, 400, 320, fill="red", lineWidth=10)
        youWin('X')
    elif q7+q6+q9 == 6:
        Line(0, 320, 400, 320, fill="red", lineWidth=10)
        youWin('O')
    elif q3+q5+q7 == 3:
        Line(400, 0, 0, 400, fill="red", lineWidth=10)
        youWin("X")
    elif q3+q5+q7 == 6:
        Line(400, 0, 0, 400, fill="red", lineWidth=10)
        youWin("O")
    
    elif alreadyTaken == True and alreadyTaken1 == True and alreadyTaken2 == True and alreadyTaken3 == True and alreadyTaken4 == True and alreadyTaken5 == True and alreadyTaken6 == True and alreadyTaken7 == True and alreadyTaken8 == True:
        youWin("tie")
    

def youWin(winner):
    global alreadyTaken1
    global alreadyTaken2
    global alreadyTaken3
    global alreadyTaken4
    global alreadyTaken5
    global alreadyTaken6
    global alreadyTaken7
    global alreadyTaken8
    global youWinVariable
    
    alreadyTaken = True
    alreadyTaken1 = True
    alreadyTaken2 = True
    alreadyTaken3 = True
    alreadyTaken4 = True
    alreadyTaken5 = True
    alreadyTaken6 = True
    alreadyTaken7 = True
    alreadyTaken8 = True
    youWinVariable = True
    
    if winner == "X" or winner == "O":
        Label(winner + "wins!", 200, 200, size=100, fill="pink", border="blue")
    elif winner == "tie":
        Label("Tie!", 200, 200, size=100, fill="pink", border="blue")
    Rect(100, 260, 200, 100)
    Label("Play Again", 200, 310, fill="white", size=30)
    
def playAgain():
    
    
    Rect(0, 0, 400, 400, fill="white")
    game()
    
    global XO
    global alreadyTaken
    global alreadyTaken1
    global alreadyTaken2
    global alreadyTaken3
    global alreadyTaken4
    global alreadyTaken5
    global alreadyTaken6
    global alreadyTaken7
    global alreadyTaken8
    global youWinVariable
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    
    XO = "X"
    q1 = 10
    q2 = 10
    q3 = 10
    q4 = 10
    q5 = 10
    q6 = 10
    q7 = 10
    q8 = 10
    q9 = 10
    alreadyTaken = False
    alreadyTaken1 = False
    alreadyTaken2 = False
    alreadyTaken3 = False
    alreadyTaken4 = False
    alreadyTaken5 = False
    alreadyTaken6 = False
    alreadyTaken7 = False
    alreadyTaken8 = False
    youWinVariable = False
    
    
    
    
    
  
    
    
print("player X goes first")
game()
