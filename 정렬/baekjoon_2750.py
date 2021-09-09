def solution(n):
    
    a = [int(input()) for _ in range(n)]
    
    return sorted(a)

if __name__ =='__main__':
    n = int(input())
    a = solution(n)
    for i in a:
        print(i)
