import sys

def dfs(depth):
    if depth == m:
        print(' '.join(map(str, solve)))
        return None
    
    for i in range(1, n+1):
        if i not in solve:
            solve.append(i)
            dfs(depth + 1)
            solve.pop()
        else:
            continue
    
       
if __name__ == "__main__":
    n,m = tuple(map(int, input().split()))
    solve = []
    
    dfs(0)
    
    
