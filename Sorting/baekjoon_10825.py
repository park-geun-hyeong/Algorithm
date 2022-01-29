import sys
read = sys.stdin.readline

def solution(score):
    return sorted(score, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
    
if __name__ == "__main__":
    n = int(input())
    score = [list(map(str, read().split())) for _ in range(n)]
    for i in solution(score):
        print(i[0])
      
