def solution(a):
    
    n = len(a)
    dp = [[0]*3 for _ in range(n)]
    
    for i in range(0, n):
        if n==0:
            dp[0] = a[0]
            
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + a[i][0] 
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + a[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + a[i][2]
        
    MIN = min(dp[n-1][0], dp[n-1][1], dp[n-1][2])   
    
    return MIN


if __name__ == '__main__':
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    
    print(solution(a))
