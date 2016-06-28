##Board Setup
board = []
quit=False
from random import randint
import winsound
#welcome
print("Welcome to Battleship 2.0\n")
print("X\'s correspond to places you have fired. O\'s are places you have not fired. *\'s are hits")

#get board and snip sizes with error handling for ship length fitting and integer type

while True:
    try:
        size=int(input("What size board would you like? 2->2x2, 3->3x3 etc...\n"))
        if size>0:
            break
        else:
            print("\nboard size must be an integer greater than 0")
    except:
        print("\nboard size must be an integer greater than 0")
        size=0
        
while True:
    try:
        ship_length=int(input('how long do you want the ship?\n'))
        if ship_length<=size:
            break
        else:
            print("\nyou must select a ship length that fits: %i or less" %size)
    except:
        print("\nship length must be an integer")
        ship_length=0
    

#build board
for x in range(size):
    board.append(["O"] * size)

#function for printing board from memory
def print_board(board):
    guide=""
    for n in range(1,len(board[0])+1):
        guide=guide+str(n)+" "
    print("  "+guide)
    print("  "+"-"*(len(board)*2-1))
    n=1
    for row in board:
        print(str(n)+"|"+str(" ".join(row))+"|")
        n=n+1
    print("  "+"-"*(len(board)*2-1))
    
#functions for picking random ship positions
def random_orientation():
    return randint(0,1)

def determ_ship_space(length,size):
    poss_ship_space=[]
    orient=random_orientation()
    if orient==0:
        for x in range(size):
            poss_ship_space.append(["@"]*(size-length+1))
    else:
        for x in range((size-length+1)):
            poss_ship_space.append(["@"]*size)
    start_row=random_row(poss_ship_space)
    start_col=random_col(poss_ship_space)
    
    ship_space=[]
    for i in range(length):
        if orient==0:
            ship_space.append([start_row,start_col+i])
        if orient==1:
            ship_space.append([start_row+i,start_col])
    return ship_space
            

def random_row(ship_space):
    return randint(0, len(ship_space) - 1)

def random_col(ship_space):
    return randint(0, len(ship_space[0]) - 1)

#start game, get ship position, print position
print("\nLet's play Battleship!\n")
print_board(board)
ship_space=determ_ship_space(ship_length,size)
print(ship_space)


##Turns

turn=0;

#loop runs while there is no quit signal
while quit==False:
    #check for win condition
    if ship_space==[]:
        winsound.PlaySound("media\\sink.wav", winsound.SND_ALIAS)
        print("Congratulations you sunk my fleet!")
        break
        
    #label turn number and initialize guesses
    print("\nTurn", turn+1)
    guess_row=""
    guess_col=""
    
    #request first guess and check for quit
    guess_row = input("Guess Row: ")
    if guess_row=="q" or guess_col=="q":
            quit=True
            break
    
    #request second guess and check for quit
    guess_col = input("Guess Col: ")
    if guess_row=="q" or guess_col=="q":
            quit=True
            break
    
    #convert each to integer and translate to code index and check each for data type
    try:
        guess_row=int(guess_row)-1
    except:
        print("Guess an integer or q to quit. Try Again.")
        guess_row = int(input("Guess Row: "))-1
    
    try:
        guess_col=int(guess_col)-1
    except:
        print("Guess an integer or q to quit. Try Again.")
        guess_col = int(input("Guess Col: "))-1
    
    winsound.PlaySound("media\\fire.wav",winsound.SND_FILENAME)
        
    #check hit miss or repeat and return resultsship
    try: 
        ship_space.remove([guess_row,guess_col])
        winsound.PlaySound("media\\hit.wav", winsound.SND_ALIAS)
        print("You hit my ship!")
        board[guess_row][guess_col] = "*"
        
    except:
        if (guess_row < 0 or guess_row > size-1) or (guess_col < 0 or guess_col > size-1):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already and missed.")
        elif(board[guess_row][guess_col] == "*"):
            print("You guessed that one already and hit.")
        else:
            winsound.PlaySound("media\\miss.wav", winsound.SND_ALIAS)
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
    turn=turn+1
    print_board(board)

#close game window

input("press ENTER to exit")