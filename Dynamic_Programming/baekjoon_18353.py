import sys 
read = sys.stdin.readline

def solution(n, soldier):
    
    dp = [0]*n
    soldier.reverse()
     
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if soldier[j]<soldier[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return int(n - max(dp))  

if __name__ == "__main__":
    n = int(input())
    soldier = list(map(int, read().split()))
    print(solution(n, soldier))
    
    
    
