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


def dfs(graph, start, visited):
    
    global cnt
    visited[start] = True
    
    for i in graph[start]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)
        else:
            continue
 
    return cnt
        
         
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    line = [list(map(int, input().split())) for _ in range(m)]
    
    visited = [False] * (n+1)
    Graph = graph(n, line)   
    
    cnt=0
    print(dfs(Graph, 1, visited))
    
