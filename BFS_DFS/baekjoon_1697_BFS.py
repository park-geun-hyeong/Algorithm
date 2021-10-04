from collections import deque
import sys

def bfs(n,k):
    
    dist = [0 for _ in range(100001)]
    queue = deque([n]) 
    
    while queue:
        
        n = queue.popleft()
        
        if n == k:
            break
    
        for nx in [n-1, n+1, 2*n]:
            if (0<= nx <100001) and (dist[nx] == False):
                dist[nx] = dist[n] + 1
                queue.append(nx)
            else:
                continue
    
    return dist[k]
        

if __name__ == "__main__":
    n,k = list(map(int, input().split()))
    print(bfs(n,k))
    
    
