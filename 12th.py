board = [" "] * 9

def print_b():
    for i in range(0, 9, 3):
        print(board[i] + "|" + board[i+1] + "|" + board[i+2])
        
def win(p):
    combos = [(0,1,2),(3,4,5),(6,7,8),
              (0,3,6),(1,4,7),(2,5,8),
              (0,4,8),(2,4,6)]
    return any(all(board[i]==p for i in c) for c in combos)

def play():
    p = "X"
    for _ in range(9):
        print_b()
        move = int(input(f"{p}'s move (1-9): ")) -1
        if board[move] == " ":
            board[move] = p
            if win(p):
                print_b()
                print(f"{p} wins!")
                return
            p = "O" if p=="X" else "X"
        else:
            print("Invalid move")
    print_b()
    print("Draw!")

play()
