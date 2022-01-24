import sys
from collections import deque
read = sys.stdin.readline
inf = sys.maxsize

def solution(n,k,x,adj_list):
    
    short_dist = [inf] * (n+1)
    short_dist[x] = 0 
    for i in adj_list[x]:
        short_dist[i] = 1
        
    node_check = [0] * (n+1)
    node_check[x] = 1
    
    q = deque([])    
    q.extend(adj_list[x])
    
    while q:
        a = q.popleft()
        node_check[a] = 1
        previous_dist = short_dist[a]
        
        link = adj_list[a]
        if len(link) == 0:
            continue
        
        for i in link:
            short_dist[i] = min(short_dist[i], previous_dist + 1)
            if node_check[i] == 0:
                q.append(i)
            
    result = []
    for idx, i in enumerate(short_dist):
        if idx == 0:
            continue
            
        else:
            if i == k:
                result.append(idx)
    
    if len(result) == 0:
        print(-1)
    else:   
        for i in result:
            print(i)



if __name__ == "__main__":
    n,m,k,x = list(map(int, input().split()))
    
    adj_list = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = list(map(int, input().split()))
        adj_list[a].append(b)
        
    solution(n,k,x,adj_list)
        
        
        
