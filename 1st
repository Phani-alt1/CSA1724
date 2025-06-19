from collections import deque

goal = [[1,2,3],[4,5,6],[7,8,0]]

def is_goal(s): return s== goal;

def find_zero(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0: return i,j

def get_moves(s):
    x,y=find_zero(s)
    dirs=[(-1,0),(1,0),(0,-1),(0,1)]
    moves = []
    for dx,dy in dirs:
        nx,ny=x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            new=[row[:] for row in s]
            new[x][y], new[nx][ny]= new[nx][ny], new[x][y]
            moves.append(new)
    return moves

def solve(start):
    q= deque()
    q.append((start,[]))
    seen=set()
    while q:
        curr, path = q.popleft()
        frozen = tuple(map(tuple,curr))
        if frozen in seen: continue
        seen.add(frozen)
        if is_goal(curr): return path+[curr]
        for next_state in get_moves(curr):
            q.append((next_state,path+[curr]))
    return None


start = [[1,2,3],[4,0,6],[7,5,8]]
result=solve(start)
for i, step in enumerate(result):
    print(f"step{i}:")
    for row in step:
        print(row)
    print()
