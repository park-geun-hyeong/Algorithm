import sys

def solution(x, c):
    
    x = sorted(x)
    n = len(x)
    d = 0
    
    start = 1
    end = x[-1] - x[0]
    
    while start <= end:
        mid = (start+end) // 2  
        
        ##전집의 위치
        before = x[0]
        
        ## 와이파이 개수
        wifi_cnt = 1
        
        for i in range(1, n):
            if x[i] >= before + mid:
                before = x[i]
                wifi_cnt += 1
               
        if wifi_cnt >= c: ## 와이파이 개수가 원하는 것보다 많다면
            start = mid + 1 ## 설치 간격을 늘려주기
            d = mid
        else: ## 와이파이 개수가 원하는 것보다 적다면
            end = mid - 1 ## 설치 간격을 좁혀주기
            
    return d
    
if __name__ == "__main__":
    
    n,c = map(int, input().split())
     
    x = [int(sys.stdin.readline()) for _ in range(n)] 
    
    print(solution(x,c))
    
