import os

# Game Board
def printBoard(X, O):
    print(f" {'X' if X[0] else ('O' if O[0] else ' ')} | {'X' if X[1] else ('O' if O[1] else ' ')} | {'X' if X[2] else ('O' if O[2] else ' ')}")
    print("---|---|---")
    print(f" {'X' if X[3] else ('O' if O[3] else ' ')} | {'X' if X[4] else ('O' if O[4] else ' ')} | {'X' if X[5] else ('O' if O[5] else ' ')}")
    print("---|---|---")
    print(f" {'X' if X[6] else ('O' if O[6] else ' ')} | {'X' if X[7] else ('O' if O[7] else ' ')} | {'X' if X[8] else ('O' if O[8] else ' ')}")

# Checking the wining and draw of the match
def checkWin(X, O):
    # wining conditions
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]]

    # checking for any condition to be satisfied or not
    for win in wins:
        if X[win[0]] + X[win[1]] + X[win[2]] == 3:
            print("Match Over!")
            print("X won the match")
            return 0
        if O[win[0]] + O[win[1]] + O[win[2]] == 3:
            print("Match Over!")
            print("O won the match")
            return 1
    
    # Checking for a draw in match
    if (X.count(0) + O.count(0)) <= 9:
        print("Match Over!")
        print("Its a draw in match")
        return 1

if __name__ =="__main__":
    X = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    O = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = True # True for X and False for O
    while True:
        print("                 Welcome to Tic Tac Toe")
        print("Help: Enter the index value of the position to enter O or X")
        printBoard(X, O)
        won = checkWin(X, O)
        if won == 1 or won == 0 or won == -1:
            break
        if turn:
            print("X's Chance")
            val = int(input("Enter the place to mark: "))
            if val > 8 or val < 0:
                os.system('clear')
                print("Error!\nEnter the correct position to be marked between the range of 0-8")
                continue
            if X[val] or O[val]:
                os.system('clear')
                print("Error!\nTheir is already a value at that position")
                continue
            X[val] = 1
        else:
            print("O's Chance")
            val = int(input("Enter the place to mark: "))
            if val > 8 or val < 0:
                os.system('clear')
                print("Error!\nEnter the correct position to be marked between the range of 0-8")
                continue
            if X[val] or O[val]:
                os.system('clear')
                print("Error\nTheir is already a value at that position")
                continue
            O[val] = 1
        turn = not turn
        os.system('clear')
        
