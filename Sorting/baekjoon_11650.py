import sys

def solution(a):
    return sorted(a[:], key=lambda x:(x[0],x[1]))


if __name__ == "__main__":
    n = int(input())
    a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    sol = solution(a)
    for i in sol:           
        print(f'{i[0]} {i[1]}')
    
