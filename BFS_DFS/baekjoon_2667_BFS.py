from collections import deque
import sys

def bfs(x,y):
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    queue = deque()
    queue.append([x,y])
    house[x][y] = 0
    cnt = 0
         
    while queue:
        
        x,y = queue.popleft()
        cnt += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx < n) and (0 <= ny < n): 
                if house[nx][ny] == 1:
                    queue.append([nx,ny])
                    house[nx][ny] = 0
        
            else:
                continue  
   
    return cnt
            
    
if __name__ == "__main__":
    n = int(input())
    if n<5 or n>25:
        raise Exception("5 <= n <= 25")
                       
    house = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
    
    num = []
    for i in range(n):
        for j in range(n):
            if house[i][j] == 1:
                 num.append(bfs(i, j))
            
                 
    print(len(num))
    for i in sorted(num):
        print(i)
     
