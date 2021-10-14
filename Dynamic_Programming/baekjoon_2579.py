def solution(s):
    dp = [] 
    
    for i in range(len(s)):
        if i == 0:
            dp.append(s[i])
            continue
        
        elif i == 1:
            dp.append(max(dp[i-1] + s[i], s[i]))
            continue
        
        elif i == 2:
            dp.append(max(s[i] + s[i-2], s[i] + s[i-1]))
            continue
            
        else:
            dp.append(max(s[i] + dp[i-2], s[i] + s[i-1] + dp[i-3]))
            
        
    return dp[-1]

if __name__ == "__main__":
    n = int(input())
    s = [int(input()) for _ in range(n)]
    print(solution(s))
