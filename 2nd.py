N=8;
count=0;
def is_safe(board, row, col):
    for i in range(row):
        if board[i]==col or \
            board[i] - i == col-row or \
            board[i] + i == col+row:
            return False
    return True
def solve_n_queens(row,board):
    global count
    if row==N:
        count+=1
        print(f"solution {count} : ")
        print_solution(board)
        return
    for col in range(N):
        if is_safe(board, row, col):
            board[row]= col
            solve_n_queens(row+1,board)
            #if solve_n_queens(row+1,board):
                #return True
    #return False

def print_solution(board):
    for i in range(N):
        row = ["."]*N
        row[board[i]] = "Q"
        print(" ".join(row))
    print()

board=[-1]*N
solve_n_queens(0,board)
print(f"Total solutions found :{count}")
