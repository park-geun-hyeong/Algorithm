def choice(wine):
    
    n = len(wine) 
    dp = [0 for _ in range(n)]
    
    for i in range(n):
        if i == 0:
            dp[i] = wine[i]
        elif i == 1:
            dp[i] = wine[0] + wine[1]
        elif i == 2:
            dp[i] = max(wine[0] + wine[1], wine[0] + wine[2], wine[1]+wine[2])
        else:
            dp[i] = max(dp[i-1], dp[i-3]+wine[i-1]+wine[i] , dp[i-2] + wine[i])
       
    ans = dp[n-1]
    return ans

if __name__ == '__main__':
    
    n = int(input())
    assert 1<=n<=10000, "1<=n<=10000"
    
    wine = [int(input()) for _ in range(n)] 
   
    print(choice(wine))
    
