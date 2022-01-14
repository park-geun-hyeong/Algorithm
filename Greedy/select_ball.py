'''
# Time Complexity: O(n^2)

def solution(ball):
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            if ball[i] != ball[j]:
                cnt += 1
    print(cnt)
    
if __name__ == "__main__":
    n,m = tuple(map(int, input().split()))
    ball = list(map(int, input().split()))
    solution(ball)
    
'''

# Time Complexity: O(n)

n,m = tuple(map(int, input().split()))
ball = list(map(int, input().split()))

dp = [0] * 11
for i in ball:
    dp[i] += 1 
    
cnt = 0 
for i in sorted(set(ball)):
    n -= dp[i]
    cnt += dp[i] * n
    
print(cnt)
    
