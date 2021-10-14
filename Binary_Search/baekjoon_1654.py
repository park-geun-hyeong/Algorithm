import sys

def solution(a, n):
    
    start = 1 ## 랜선 길이의 최솟값
    end = a[-1] ## 랜선 길이의 최댓값
    result = 0
    
    while start <= end:
        mid = (start+end) // 2 ## 임의의 랜선길이
        
        num = sum([(i//mid) for i in a]) ## 임의의 랜선길이로 각각의 랜선을 잘랐을 때 
                
        if num >= n: ## 원하는 것보다 랜선이 많이 잘렸다 ==> 좀더 크게 자를 수 있다.
            start = mid + 1
            result = mid ## n 개보다 많이 잘릴 경우도 인정하므로
            
        else:  ## 원하는 것보다 랜선이 적게 잘렸다 ==> 좀더 작게 잘라야 한다.
            end = mid - 1 
    
    return result
    
if __name__ == "__main__":
    k,n = map(int, sys.stdin.readline().split())
    
    if k>n:
        raise Exception("k <= n")
        
    a = [int(sys.stdin.readline()) for _ in range(k)]
    print(solution(sorted(a),n))
