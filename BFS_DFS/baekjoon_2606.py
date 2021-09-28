from collections import deque
import sys

def graph(n, line):
    Graph = [[] for _ in range(n+1)]
    
    for j in line:
        for i in range(1, n+1):
            if j[0] == i:
                Graph[i].append(j[1])
            elif j[1] == i:
                Graph[i].append(j[0])
            else: 
                continue
         
    return [sorted(i) for i in Graph]


def bfs(graph,start, visited):
    
    queue = deque([start])
    visited[start] = True
    
    b=[]
    while queue:
        v = queue.popleft()
        b.append(v)
        #print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] =True
        
    return len(b)-1
        
         
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    line = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    
    visited = [False] * (n+1)
    Graph = graph(n, line)   
    
    print(bfs(Graph, 1, visited))
    
