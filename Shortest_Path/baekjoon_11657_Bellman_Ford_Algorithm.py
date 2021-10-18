import sys
inf = sys.maxsize
read = sys.stdin.readline

def short(start,n):
    
    dist[start] = 0
   
    for _ in range(n):
        for i in range(1, n+1):
            if dist[i] == inf:
                    continue
                    
            linked = graph[i]
            for j in linked:

                cost = dist[i] + j[1]
                if cost < dist[j[0]]:
                    dist[j[0]] = cost
    breaker=False
    for i in range(1, n+1):
        if dist[i] == inf:
            continue
        
        linked = graph[i]
        for j in linked:
            cost = dist[i] + j[1]
            if cost < dist[j[0]]:
                dist[j[0]] = cost
                return False
                breaker = True
            
            if breaker:
                break
    
    return True
    

if __name__ == "__main__":
    n,m = map(int, input().split())
    
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a,b,c = map(int, read().split())         
        graph[a].append((b,c))
        
    dist = [inf for _ in range(n+1)]
    
    start = 1
    if short(start,n):
        for i in range(2, n+1):
            print(-1 if dist[i] == inf else dist[i])
    else:
        print(-1)
