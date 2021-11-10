import sys
from collections import deque
read = sys.stdin.readline

def bfs(graph, parent):
    
    queue = deque()
    queue.append(1)
    
    while queue:
        node = queue.popleft()
        
        for i in graph[node]:
            if parent[i] == 0:
                parent[i] = node
                queue.append(i)
            else:
                continue
                
        
if __name__ == "__main__":
    
    n = int(input())
    graph = [[] for _ in range(n+1)]
    
    for _ in range(n-1):
        a,b = list(map(int, read().split()))
        graph[a].append(b)
        graph[b].append(a)
     
    parent=[0 for _ in range(n+1)]
    bfs(graph, parent)
    
    for i in range(2, n+1):
        print(parent[i])
        

