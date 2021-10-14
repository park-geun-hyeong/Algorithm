def solution(t):
    n=len(t)
    dp = [[0]*i for i in range(1,n+1)]
       
    for i in t:
        z = len(i)
        if z == 1:
            dp[z-1] = i
            continue
            
        else: 
            for j in range(z):
                if j == 0:
                    dp[z-1][0] = t[z-1][0] + dp[z-2][0]
                elif j == int(z-1):
                    dp[z-1][j] = t[z-1][j] + dp[z-2][j-1]
                else:    
                    dp[z-1][j] = max(t[z-1][j] + dp[z-2][j-1], t[z-1][j] + dp[z-2][j])

                
    return max(dp[-1])

if __name__ == '__main__':
    n = int(input())
    t = [list(map(int, input().split())) for _ in range(n)]
    print(solution(t))
