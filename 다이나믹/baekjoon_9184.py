import sys
#input = sys.stdin.readline

max = 21
dp = [[[0]*max for _ in range(max)] for _ in range(max)]

def solution(a, b, c):
      
    if (a<=0) or (b<=0) or (c<=0):
        return 1
     
    if (a>20) or (b>20) or (c>20):
        return solution(20,20,20)    
    
    if dp[a][b][c]:
        return dp[a][b][c]

    if a<b<c:
        dp[a][b][c] = solution(a,b,c-1) + solution(a,b-1,c-1) - solution(a,b-1,c)
        
        return dp[a][b][c]
    
    dp[a][b][c] = solution(a-1,b,c) + solution(a-1, b-1, c) + solution(a-1,b,c-1) - solution(a-1, b-1, c-1)
    
    return dp[a][b][c]

if __name__ == '__main__':
    li=[]
    while True:       
        a = list(map(int ,input().split()))
        
        try:
            if (a[0] == -1) and (a[1] == -1) and (a[2] == -1):
                break
            
            if (a[0]>50 or a[1]>50 or a[2]>50) or (a[0]<-50 or a[1]<-50 or a[2]<-50):
                raise Exception
        
            li.append(a)
        except Exception as e:
            print("-50<= a,b,c <=50")
            
    for i in li:
        w = solution(i[0],i[1],i[2])
        print(f"w({i[0]},{i[1]},{i[2]}) = {w}")

