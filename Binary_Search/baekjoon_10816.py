import sys
from collections import defaultdict

def default_factory():
    return int(0)

def final(a, b):
    dic=defaultdict(default_factory)
    
    for i in a: 
        try:
            dic[i] += 1
        except KeyError:
            dic[i] = 1
    
    return [dic[i] for i in b] 
    
if __name__ == '__main__':      

    n = int(input())
    a = list(map(int, sys.stdin.readline().split()))

    m = int(input())
    b = list(map(int, sys.stdin.readline().split()))

    for i in final(a, b):
        print(i, end = ' ')
