def solution(n):
    
    dp = [0]*101
    
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1 
    
    for i in range(4, n+1):
        dp[i] = dp[i-2] + dp[i-3]
        
    return dp[n]

if __name__ == "__main__":
    try:
        n = int(input())   
        if (n<1 or n>100):
            raise Exception
            
    except Exception as e:
        print("1<= n <= 100")
        
        
    a = [int(input()) for _ in range(n)]

    for i in a:
        print(solution(i))
