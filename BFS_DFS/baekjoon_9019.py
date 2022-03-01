import sys
from collections import deque
read = sys.stdin.readline

def D(a):
    a = (int(a)*2)%10000
    return a

def S(a):
    a-=1
    if a == -1:
        a = 9999
    return a

def L(a):
    a = str(a) 
    if len(a)<4:
        a = '0' * (4-len(a)) + a
    
    new = ''
    for idx in (1,2,3,0):
        new+=a[idx]

    return int(new)

def R(a):
    a = str(a) 
    if len(a)<4:
        a = '0' * (4-len(a)) + a
    
    new = ''
    for idx in (3,0,1,2):
        new+=a[idx]
        
    return int(new)

def next_state(idx):
    if idx == 0:
        return 'D'
    if idx == 1:
        return 'S'
    if idx == 2:
        return 'R'
    if idx == 3:
        return 'L'
    
    
def solution(a,b):
    
    STR = ''
    q = deque([[a,STR]])
    check = [0]*10001
    check[a] = 1
    
    while q:
        x, state = q.popleft()
        
        for idx, nx in enumerate([D(x), S(x), R(x), L(x)]):
            if nx == b:
                return state + next_state(idx)
            
            if check[nx] == 0:
                q.append([nx, state + next_state(idx)])
                check[nx] = 1
        
    return


if __name__ == "__main__":
    t = int(input())
    ans = [] 
    for _ in range(t):
        a,b = map(int, input().split())
        ans.append(solution(a,b))
    
    for i in ans:
        print(i)
