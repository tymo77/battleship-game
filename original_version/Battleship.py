from random import randint
import winsound

##Board Setup
board = []
quit=False

print("Welcome to Battleship\n")
print("X\'s correspond to places you have fired. O\'s are places you have not fired. *\'s are hits")
size=int(input("What size board would you like? 2->2x2, 3->3x3 etc...\n"))

for x in range(size):
    board.append(["O"] * size)

def print_board(board):
    print("-"*(len(board)*2-1))
    for row in board:
        print(" ".join(row))
    print("-"*(len(board)*2-1))

print("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row+1)
print (ship_col+1)

##Turns

turn=0;

#loop runs while there is no quit signal
while quit==False:
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
    
    #convert each to integer and check each for data type
    try:
        guess_col=int(guess_col)-1
    except:
        print("Guess an integer or q to quit. Try Again.")
        guess_col = int(input("Guess Col: "))-1
    try:
        guess_row=int(guess_row)-1
    except:
        print("Guess an integer or q to quit. Try Again.")
        guess_row = int(input("Guess Row: "))-1
    
    winsound.PlaySound("C:\\Users\\Tyler\\fire.wav",winsound.SND_FILENAME)
        
    #check hit mit or repeat and return results
    if guess_row == ship_row and guess_col == ship_col:
        winsound.PlaySound("C:\\Users\\Tyler\\hit.wav", winsound.SND_ALIAS)
        print("Congratulations! You sunk my battleship!")
        board[guess_row][guess_col] = "*"
        print_board(board)
        break
    else:
        if (guess_row < 0 or guess_row > size-1) or (guess_col < 0 or guess_col > size-1):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            winsound.PlaySound("C:\\Users\\Tyler\\miss.wav", winsound.SND_ALIAS)
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
    turn=turn+1
    print_board(board)

#close game window
input("press ENTER to exit")