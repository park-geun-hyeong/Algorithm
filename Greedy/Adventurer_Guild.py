import sys
read = sys.stdin.readline

def solution(scary):
    
    scary = sorted(scary)
    ans=[]
    new=[]
    for i in range(n):
        num = scary[i]
        new.append(num)
        if len(new) >= num:
            ans.append(new)
            new =[]
            
    print(len(ans))

if __name__ == "__main__":
    n = int(input())
    assert 1<= n <= 10e4
    scary = list(map(int, input().split()))
    
    solution(scary)
    
    
