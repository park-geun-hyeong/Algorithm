def lis(li):
    
    n = len(li)
    dp = [0 for _ in range(n)] #dp[i] = li[i]가 맨 마지막 원소일떄의 최대 증가수열 길이
    
    MAX = 1
    for i in range(n):
        if i == 0:
            dp[i] = 1
            continue
        
        val = 0    
        for j in range(0, i):
            if li[j] < li[i]:
                if val < dp[j]:
                    val = dp[j]
                    
        dp[i] = val + 1
        if MAX<dp[i]:
            MAX=dp[i]
            
    #MAX = max(dp)
    print(MAX)

if __name__ == "__main__":
    n = int(input())
    assert 1<=n<=1000
    
    li = list(map(int, input().split()))
    
    lis(li)
    
