import sys

def solution(a, m):
    
    a = sorted(a)
    start = 1
    end = a[-1]  
    
    h = 0
    while start<=end:
        mid = (start+end) // 2
        
        if sum([i-mid if i>=mid else int(0) for i in a]) < m:
            end = mid-1
            
        else:
            start = mid + 1
            h = mid  
        
    return h
    
if __name__ == "__main__":
    n,m = map(int, input().split())
        
    a = list(map(int, sys.stdin.readline().split()))
    
    if sum(a)< m:
        raise Exception
        
    print(solution(a,m))
