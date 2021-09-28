from collections import deque
import sys

def dfs(x,y):
    
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    global cnt
    if house[x][y] == 1:
        
        cnt += 1
        house[x][y] = 0
        
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)    
        return True  
    
    return False


if __name__ == "__main__":
    n = int(input())
    if n<5 or n>25:
        raise Exception("5 <= n <= 25")
                       
    house = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
    
    num = []
    result=0
    cnt = 0
    for i in range(n):
        for j in range(n):
            if dfs(i,j) == True:
                num.append(cnt)
                result += 1
                cnt = 0
                
    print(result)
    for i in sorted(num):
        print(i)
     
