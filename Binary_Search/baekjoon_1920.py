import sys

def final(a, b):
    return ['1' if i in set(a) else '0' for i in b]
    
if __name__ == '__main__':      

    n = int(input())
    a = list(map(int, sys.stdin.readline().split()))

    m = int(input())
    b = list(map(int, sys.stdin.readline().split()))

    for i in final(a, b):
        print(i)
