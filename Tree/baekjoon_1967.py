import sys
read = sys.stdin.readline
sys.setrecursionlimit(20000)

def dfs(start, visited):

    linked = tree[start]
    for node, weight in linked:
        if visited[node] == 0:
            visited[node] = visited[start] + weight
            dfs(node, visited)
            
if __name__ == "__main__":
    n = int(input()) 
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        p,c,w = tuple(map(int, input().split()))
        tree[p].append((c,w))
        tree[c].append((p,w))
        
    visited = [0] * (n+1)
    dfs(1, visited)
    visited[1] = 0
    
    max_idx = 0
    max_dist = 0
    for idx, i in enumerate(visited):
        if i> max_dist:
            max_dist = i
            max_idx = idx
            
    visited2 = [0] * (n+1)
    dfs(max_idx, visited2)
    visited2[max_idx] = 0
    print(max(visited2))
    
    
