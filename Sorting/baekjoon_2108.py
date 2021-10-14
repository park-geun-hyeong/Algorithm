import sys
from collections import Counter

def solution(n):
    
    a = [int(sys.stdin.readline()) for _ in range(n)]
    avg = round(sum(a)/len(a))
    center = sorted(a)[len(a)//2]
    
    if list(Counter(a).values()).count(max(Counter(a).values())) == 1:
        many = Counter(a).most_common(1)[0][0]
    else:
        many = sorted(Counter(a).most_common(list(Counter(a).values()).count(max(Counter(a).values()))), key = lambda x : x[0])[1][0]   
    
    sub = max(a)-min(a)
    
    return [avg, center, many, sub]

if __name__ =='__main__':
    
    try:
        n = int(input())
        if n%2 == 0:
            raise Exception
    except Exception as e:
        print("Error")
        
    for i in solution(n):
        print(i)
