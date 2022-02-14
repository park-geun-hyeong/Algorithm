import sys 
from itertools import combinations
read = sys.stdin.readline

def solution(n,k,color):
    
    if k == 1:
        return 0

    groups = list(combinations(list(range(1,k+1), 2))
    MIN = 10e9
    
    # 꼭 두 좌표를 꼭짓점으로 가지는 직사각형일 필요는 없다.
    for one, two in groups:
        colors = set(i for i in range(1,k+1))
        in_check = [0] * (k+1)
        in_check[one] = 1
        in_check[two] = 1
        
        group1 = color[one]
        group2 = color[two]
        
        residual = list(colors - {one, two})
        
        for x1,y1 in group1:
            for x2,y2 in group2:
                area = abs(x1-x2) * abs(y1-y2)
                
                for c in residual:
                    for x3,y3 in color[c]:
                        if (x1<=x3<=x2 or x2<=x3<=x1) and (y1<=y3<=y2 or y2<=y3<=y1):
                            in_check[c] = 1
                            break
                
                if sum(in_check) == k:
                    MIN = min(MIN, area)
                    
    return MIN


if __name__ == "__main__":
    n,k = list(map(int, input().split()))
 
    color = [[] for _ in range(k+1)]
    for _ in range(n):
        X,Y,K = list(map(int,input().split()))
        color[K].append([X,Y])


    print(solution(n,k,color))
    
    
    
