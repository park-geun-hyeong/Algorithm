import sys 
read  = sys.stdin.readline

def solution(N):
    length = len(N)
    
    first = sum([N[i] for i in range(length // 2)])
    second = sum([N[i] for i in range(length // 2, length)])
    
    if first == second:
        print("LUCKY")
    else:
        print("READY")

if __name__ == "__main__":
    N = list(map(int, read().rstrip()))
    solution(N)
