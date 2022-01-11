import sys 
from itertools import combinations
read = sys.stdin.readline

def solution(graph):
    ans = []
    
    case = list(combinations(range(n), n//2))
    
    for i in case:
        SUM1 = 0
        SUM2 = 0
        
        another = set(range(n)) - set(i)
        
        for j in i:
            for k in i:
                SUM1 += graph[j][k]
        
        for j in another:
            for k in another:
                SUM2 += graph[j][k]
                                
        ans.append(abs(SUM1 - SUM2))
                       
    return ans

if __name__ == "__main__":
    n = int(input())
    assert (n%2==0) and (4<=n<=20) 
    
    graph = [list(map(int, read().split())) for _ in range(n)]
    ans = solution(graph)
    print(min(ans))
    
    
