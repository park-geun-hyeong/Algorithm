def dfs(depth):
    if depth == m:
        print(' '.join(map(str, solve)))
        return
    
    else:
        for i in range(1, n+1):
            solve.append(i)
            dfs(depth + 1)
            solve.pop()
            
if __name__ == "__main__":
    n,m = tuple(map(int, input().split()))
    solve=[]
    dfs(0)
    
