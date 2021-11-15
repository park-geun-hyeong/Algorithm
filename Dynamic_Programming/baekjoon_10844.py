def stair(n):
    
    num = int(1e9) 
    dp = [[0]*10 for _ in range(101)]
    
    # dp[i][j] => 길이가 i이고 i번째 자리수의 숫자가 j인 경우의 수
    
    for i in range(1,10):
        dp[1][i] = 1
        
    for i in range(2, 101):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
            
            elif j == 9:
                dp[i][j]= dp[i-1][8]
                
            else: 
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]  
    
    ans = sum(dp[n])  
    
    return ans%num

if __name__ == "__main__":
    
    n = int(input())
    if n<1 or n>100:
        raise Exception("0<=n<=100")
             
    print(stair(n))
