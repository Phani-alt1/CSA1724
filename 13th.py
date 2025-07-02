board = [' '] * 9

def win(p):
    c = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(all(board[i]==p for i in combo) for combo in c)

def draw():
    return ' ' not in board

def minimax(is_max):
    if win('O'): return 1
    if win('X'): return -1
    if draw(): return 0
    if is_max:
        best = -2
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(False))
                board[i] = ' '
        return best
    else:
        best = 2
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(True))
                board[i] = ' '
        return best

def ai_move():
    best, move = -2, -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best:
                best, move = score, i
    board[move] = 'O'

def print_board():
    for i in range(0,9,3):
        print('|'.join(board[i:i+3]))
    print()

while True:
    print_board()
    x = int(input("Your move (1-9): ")) - 1
    if board[x] != ' ':
        print("Invalid")
        continue
    board[x] = 'X'
    if win('X'):
        print_board()
        print("You win!")
        break
    if draw():
        print_board()
        print("Draw!")
        break
    ai_move()
    if win('O'):
        print_board()
        print("AI wins!")
        break
    if draw():
        print_board()
        print("Draw!")
        break
