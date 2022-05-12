import sys
from collections import deque
from copy import deepcopy
from itertools import combinations
read = sys.stdin.readline
MIN = sys.maxsize

def bfs(case):
    global adj_list, seq 
    check = [0]*(n+1)
    
    check[case[0]] = 1
    
    q = deque([case[0]])
    summation = seq[case[0]]
    num = 1
    while q:
        area = q.popleft()
        
        adj = adj_list[area]
        for i in adj:
            if (check[i] == 0) and (i in case):
                check[i] = 1
                num += 1
                summation += seq[i] 
                q.append(i)
        
    return summation, num

if __name__ =="__main__":
    n = int(read().rstrip())
    seq = [0] + list(map(int, read().split()))
    adj_list = [[] for _ in range(n+1)] 
    for i in range(1, n+1):
        data = list(map(int, read().split()))
        if data == 0:
            continue
        adj_list[i] += data[1:]
    
    for i in range(1, n//2 + 1):
        cases = list(combinations(range(1,n+1),i))
        
        for case in cases:
            sum1, length1 = bfs(case)
            sum2, length2 = bfs([i for i in range(1,n+1) if i not in case])
            
            if length1 + length2 == n:
                MIN = min(MIN, abs(sum1 - sum2))   
                if MIN == 0:
                    print(0)
                    sys.exit()
    
    
    if MIN == sys.maxsize:
        print(-1)
    else:
        print(MIN)
    
