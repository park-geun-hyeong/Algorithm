import sys
from collections import deque
from copy import deepcopy
read = sys.stdin.readline

def loc(i, x):
    if i == 0:
        return x-1
    
    if i == 1:
        return x + 1
    
    if i == 2:
        return 2*x

def get_trace(trace, nx):
    return []
    

def solution(n,k):
    check = [0] * 100001
    
    q = deque([])
    q.append([[0,n], [n]])
    check[n] = 1
    
    while q:
        p, trace = q.popleft()
        time, x = p
      
        for i in range(3):
            nx = loc(i,x)
            if nx == k:
                trace.append(nx)
                return time+1, trace
                      
            if 0<=nx<=100000 and check[nx] != 1:          
                q.append([[time+1, nx], trace + [nx]])
                check[nx] = 1
                
if __name__ == "__main__":
    n,k = map(int, input().split())
    if n>k:
        print(n-k)
        for i in range(n,k-1,-1):
            print(i, end =' ')
        sys.exit()
    elif n == k:
        print(0)
        print(n)
        sys.exit()
    
    time, trace = solution(n,k)

    print(time)
    for i in trace:
        print(i, end = " ")
