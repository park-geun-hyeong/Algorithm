import sys
from collections import deque
read = sys.stdin.readline
            
def solution(n,k,q, s,x,y):
   
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1] 
    time= 0
    
    cnt = 1
    while q:
        virus_loc = q.popleft()
        a=[]
        for row,col in virus_loc:
            for i in range(4):
                nrow = row + drow[i]
                ncol = col + dcol[i]
                if 0<=nrow<n and 0<=ncol<n and graph[nrow][ncol] == 0:
                    graph[nrow][ncol] = cnt
                    a.append([nrow, ncol])              
        q.append(a)
        cnt += 1
        
        if cnt>k:
            cnt = 1
            time +=1
       
        if time == s:
            print(graph[x-1][y-1])
            return

if __name__ == "__main__":
    n,k = list(map(int, input().split())) 
    graph = []
    q = deque([[] for _ in range(k)]) 
    for i in range(n):
        graph.append(list(map(int, input().split())))
        
        for j in range(n):
            if graph[i][j] != 0:
                q[graph[i][j] - 1].append([i,j])
            
    s,x,y = list(map(int, input().split()))   
    solution(n,k, q,s,x,y)
    
