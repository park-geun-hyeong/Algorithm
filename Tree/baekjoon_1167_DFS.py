import sys
from collections import deque
read = sys.stdin.readline
            
def dfs(start, visited):
    for v,e in tree[start]:
        if visited[v] == 0:
            visited[v] = visited[start] + e
            dfs(v, visited)    
    
if __name__ == "__main__":    
    V = int(input())
    d = [list(map(int, read().split()))  for _ in range(V)]
    
    tree=[[] for _ in range(V+1)]
    for i in d:
        LEN = len(i)
        for j in range(1, LEN - 1, 2):
            tree[i[0]].append((i[j], i[j+1]))

    visited = [0] * (V+1)
    
    dfs(1, visited)
    visited[1] = 0
    
    maxdist=0
    maxidx=0
    for idx, i in enumerate(visited):
        if i>maxdist:
            maxdist = i
            maxidx = idx
            
    visited2 = [0] *(V+1)
    
    dfs(maxidx, visited2)
    visited2[maxidx] = 0
    print(max(visited2))
    
        
    
