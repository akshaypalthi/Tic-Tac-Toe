def display(board):
    print(board[7] + '|' + board[8] + '|' +board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])
def player1():
    index=int(input("p1: enter the loc :"))
    if (1>index or index>9):
        index=int(input("p2: enter the loc :"))
    default[index]=p1
    display(default)
    if win_check(default,p1):
        print(f"{np1} won")
        end()
def player2():
    index=int(input("p2: enter the loc :"))
    if (1>index or index>9):
        index=int(input("p2: enter the loc :"))
    default[index]=p2
    display(default)
    if win_check(default,p2):
        print(f"{np2} won")
        end()

def user():
    global p1, p2
    global np1, np2
    np1 = input("Enter player one's name: ")
    np2 = input("Enter player two's name: ")
    
    while True:
        p1 = input("Player 1, choose the symbol 'X' or 'O': ").upper()
        if p1 == 'X' or p1 == 'O':
            p2 = 'O' if p1 == 'X' else 'X'
            display(default)
            break
        else:
            print('Please enter a valid token (X or O)')

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark))
   

default=['0','1','2','3','4','5','6','7','8','9']

user()  
for i in range(0,9):
    player1()
    player2()
    
    
 
