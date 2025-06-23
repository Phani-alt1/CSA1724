from collections import deque

def is_valid(h,c):
    return (h==0 or h>=c) and (3-h==0 or 3-h>=3-c)

def solve():
    start =(3,3,1)
    goal =(0,0,0)
    moves =[(1,0),(2,0),(0,1),(0,2),(1,1)]
    visited =set()
    queue =deque([(start,[])])

    while queue:
        (h,c,b),path=queue.popleft()
        if(h,c,b) in visited: continue
        visited.add((h,c,b))
        path=path+[(h,c,b)]
        if(h,c,b)==goal: return path

        for dh,dc in moves:
            if b:
                nh,nc,nb =h-dh,c-dc,0
            else:
                nh,nc,nb=h+dh,c+dc,1
            if 0<=nh<=3 and 0<=nc<=3 and is_valid(nh,nc):
                queue.append(((nh,nc,nb),path))
    return None

path=solve()
for i,(h,c,b) in enumerate(path):
    hl,cl=h,c
    hr,cr=3-h,3-c
    side ="Left" if b else "Right"
    print(f"Step {i}: Left: {hl}H {cl}C | Right: {hr}H {cr}C | Boat: {side}")
