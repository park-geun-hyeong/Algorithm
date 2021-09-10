#import sys
#input = sys.stdin.readline
def solution(n):
    dp = [0]*1000000

    dp[0]=1
    dp[1]=2
    
    for i in range(2, n):
        dp[i] = (dp[i-1]+dp[i-2])%15746
        
    return dp[n-1]
 
if __name__ == "__main__":
    n = int(input())   
    print(solution(n))
