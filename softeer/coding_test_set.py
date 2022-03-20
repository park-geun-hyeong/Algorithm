import sys
read = sys.stdin.readline

def possible(num):
    S = [0]*n 
    S[0] = C[0]

    for i in range(n-1):
        if S[i] >= num:
            S[i+1]  = C[i+1] + D[i]
        elif S[i] + D[i] >= num:
            S[i+1] = C[i+1] + (S[i]+D[i] - num)
        else:
            return False

    if S[n-1] >= num:
        return True
    return False


def binary_search(start, end):
    
    if start == end: # End of Recursive
        return start
    mid = (start + end + 1) // 2
    if possible(mid):
        return binary_search(mid, end) # mid값을 포함하여 binary search 수행해야 함
    else:
        return binary_search(start, mid - 1)

n,t = map(int, read().split())
for _ in range(t):
    C=[0]*n
    D=[0]*n
    
    case = list(map(int, read().split()))
    for i in range(n-1):
        C[i] = case[i*2]
        D[i] = case[i*2 + 1]

    C[n-1] = case[-1]
    print(binary_search(0, int(2 * 1e12)))


