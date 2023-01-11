import os    

print("*********************************WELCOME TO TIC-TAC-TOE************************")
player1=input("player-1 please enter your name: ")
player2=input("player-2 please enter your name: ")
print("hy!",player1,"and",player2)
print(player1,"your symbol is [X] .....",player2,"your symbol is  [O]\n")

board = board = [' ' for x in range(10)]   
player = 1    
   
#the  conditions for game winning
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
 
Game = Running    
Mark = 'X'    
   
#This Function Draws Game Board    
def drawboard():    
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
   
#This Function Checks position is empty or not    
def CheckPosition(x):    
    if(board[x] == ' '):    
        return True    
    else:    
        print("please enter the valid number")    
    return False
#This Function Checks player has won or not    
def CheckWin():    
    global Game    
    #Horizontal winning condition    
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game = Win    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = Win    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = Win    
    #Vertical Winning Condition    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Win    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game=Win    
    #Diagonal Winning Condition    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = Win    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game=Win    
    #Match Tie or Draw Condition    
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
        Game=Draw    
    else:            
        Game=Running    
    

# Assigning the turns to the players

while(Game == Running):    
     
    drawboard()    
    if(player % 2 != 0):    
        print("it is ",player1," turn")    
        Mark = 'X'    
    else:    
        print("it is ",player2," turn")    
        Mark = 'O'    
    choice = int(input("Enter the position between [1-9] where you want to mark : "))    
    if(CheckPosition(choice)):    
        board[choice] = Mark    
        player+=1    
        CheckWin()    
    

drawboard()    
if(Game==Draw):    
    print("Oops! The Game Draw")    
elif(Game==Win):    
    player-=1    
    if(player%2!=0):    
        print("Congrajulations",player1,"You Won!")    
    else:    
        print("Congrajulations",player2 ,"You Won!")    