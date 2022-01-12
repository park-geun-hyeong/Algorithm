import sys 
from itertools import combinations
read = sys.stdin.readline

def cal_team(member:set):
    Sum = 0
    for i in member:
        for j in member:
            Sum+=graph[i][j]
    
    return Sum

def solution(graph):
    global MIN
    
    case = list(combinations(range(n), n//2))
    
    for i in case:
        another = set(range(n)) - set(i)
        Sub = cal_team(set(i)) - cal_team(another)
        if abs(Sub) < MIN:
            MIN = abs(Sub)

if __name__ == "__main__":
    n = int(input())
    assert (n%2==0) and (4<=n<=20) 
    
    graph = [list(map(int, input().split())) for _ in range(n)]
    MIN = 10e9
    solution(graph)
    print(MIN)
    
    
