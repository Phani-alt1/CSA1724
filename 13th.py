b = [' '] * 9
w = lambda p: any(all(b[i]==p for i in c) for c in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)])
d = lambda: ' ' not in b

def mm(m):  # minimax
    if w('O'): return 1
    if w('X'): return -1
    if d(): return 0
    scores = []
    for i in range(9):
        if b[i]==' ':
            b[i] = 'O' if m else 'X'
            scores.append(mm(not m))
            b[i] = ' '
    return max(scores) if m else min(scores)

def ai():
    best, move = -2, -1
    for i in range(9):
        if b[i]==' ':
            b[i] = 'O'
            score = mm(False)
            b[i] = ' '
            if score > best: best, move = score, i
    b[move] = 'O'

while True:
    print('\n'.join('|'.join(b[i:i+3]) for i in range(0,9,3)))
    x = int(input("Move (1-9): ")) - 1
    if b[x]!=' ': print("Invalid"); continue
    b[x]='X'
    if w('X'): print("You win!"); break
    if d(): print("Draw!"); break
    ai()
    if w('O'): print('\n'.join('|'.join(b[i:i+3]) for i in range(0,9,3))); print("AI wins!"); break
    if d(): print("Draw!"); break
