import sys
read = sys.stdin.readline

def solution(n,time, An, Bn):
    
    dp = [[0]*n for _ in range(2)]
    time.append([An,Bn])

    dp[0][0] = time[0][0]
    dp[1][0] = time[0][1]
    
    
    for i in range(1,n):
        dp[0][i] = min(dp[0][i-1] , dp[1][i-1] + time[i-1][3]) + time[i][0]
        dp[1][i] = min(dp[1][i-1] , dp[0][i-1] + time[i-1][2]) + time[i][1]
    
    return min([i[n-1] for i in dp])
    

if __name__ == "__main__":
    n = int(input())
    time = [list(map(int, read().split())) for _ in range(n-1)]
    An, Bn = map(int,read().split())
    if n == 1:
        print(min(An,Bn))
        sys.exit()
    print(solution(n,time,An,Bn))
