import sys
read = sys.stdin.readline
sys.setrecursionlimit(30000)

MAX = 0
def dfs(check, n, row,col):
    global graph,dp,dp_check
    dp_check[row][col] = 1
        
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]
    num = graph[row][col]
    
    for i in range(4):
        depth = 1
        nrow = row + drow[i]
        ncol = col + dcol[i]
        
        if 0<=nrow<n and 0<=ncol<n:
            if graph[nrow][ncol] > num and check[nrow][ncol] == 0:
                if dp_check[nrow][ncol] == 1:
                    dp[row][col] = max(dp[row][col], depth + dp[nrow][ncol])
                    continue
                
                check[nrow][ncol] = 1
                cnt = dfs(check, n, nrow,ncol)
                check[nrow][ncol] = 0
                depth += cnt
                dp[row][col] = max(dp[row][col], depth)
    
    return dp[row][col]

if __name__ == "__main__":
    n = int(input())
    graph = [list(map(int, read().split())) for _ in range(n)]
    
    check = [[0]*n for _ in range(n)]
    dp = [[1]*n for _ in range(n)] 
    dp_check = [[0]*n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if dp_check[row][col] == 0:
                check[row][col] = 1              
                dfs(check, n,row,col) 
                check[row][col] = 0
            MAX = max(MAX, dp[row][col])
    print(MAX)
