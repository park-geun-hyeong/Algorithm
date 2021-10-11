from collections import deque
import sys

def graph(v, line):
    Graph = [[] for _ in range(v+1)]
    
    for i in line:
        Graph[i[0]].append(i[1])
        Graph[i[1]].append(i[0])
        
    return Graph
    
def bfs(start):
    
    color='black'
    queue = deque([start])
    visited[start] = color 
    
    while queue:
        
        x = queue.popleft()      
        
        if visited[x] =='black':
            color = 'red'
        else:
            color = 'black' 
            
        linked = Line[x]
        
        for i in linked:
            if visited[i] == 0:
                visited[i] = color
                queue.append(i)
            
            else:
                if visited[i] == visited[x]:
                    return False
    return True

if __name__ == "__main__":
    k = int(input())
    
    ans=[]
    for _ in range(k):
        v,e = list(map(int, sys.stdin.readline().split()))
        line = [list(map(int, sys.stdin.readline().split())) for _ in range(e)]
        
        visited = [0 for _ in range(v+1)]
        Line = graph(v,line)
        
        isTrue = True
        for i in range(1,v+1): ## 떨어져 있는 노드도 생각해주기!!
            if visited[i] == 0:
                if not bfs(i):
                    isTrue = False
                    break
                    
        ans.append('YES' if isTrue else "NO")
            
        
    for i in ans:
        print(i)
    
