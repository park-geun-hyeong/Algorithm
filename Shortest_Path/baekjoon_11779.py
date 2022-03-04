import sys
from collections import deque
import heapq
read = sys.stdin.readline
inf = sys.maxsize

def get_path(start,end, path):
    
    ans = [end]
    cnt = 1
    while True:
        ans.append(path[end])
        cnt += 1
        end = path[end]
        if end == start:
            break
            
            
    return cnt, ans[::-1]
        

def solution(n,m,bus, start,end):
           
   #check = [0]*(n+1)
    state = [inf]*(n+1)
    path = [0]*(n+1)
    state[start] = 0
    #q = deque([start])
    q = []
    heapq.heappush(q, (0,start))
    while q:
        dist, s_point = heapq.heappop(q)
        
        if state[s_point] < dist:
            continue
        
        linked = bus[s_point]
        
        for e_point, cost in linked:
            cost = dist + cost
            if state[e_point]>cost:
                state[e_point] = cost
                heapq.heappush(q, (cost,e_point))
                path[e_point] = s_point
            
    cnt, Path = get_path(start,end,path)
    
    
    return state[end], cnt, Path

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    
    bus = [[] for _ in range(n+1)]
    for _ in range(m):
        s,e,c = map(int, read().split())
        bus[s].append([e,c])
        
    start, end = map(int, read().split())
    
    MIN, cnt, path = solution(n,m,bus,start,end)
    print(MIN)
    print(cnt)
    for i in path:
        print(i, end = ' ')
