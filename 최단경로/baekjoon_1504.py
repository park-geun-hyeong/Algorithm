import heapq
import sys
read = sys.stdin.readline
inf = sys.maxsize

def short(start, end):
    
    distance = [inf for _ in range(n+1)]
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        
        dist, new = heapq.heappop(q)
        
        if distance[new] < dist:
            continue
               
        linked = graph[new]
        
        for i in linked:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance[end]
            

if __name__ == "__main__":
    n,e = map(int, input().split()) 
    graph = [[] for _ in range(n+1)]
    
    for _ in range(e):
        a,b,c = map(int, read().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
          
    v1, v2 = map(int, input().split())
       
    start = 1
    case1 = [[start,v1], [v1,v2], [v2,n]]
    case2 = [[start,v2], [v2,v1], [v1,n]]
    
    ans = min(sum([short(i[0],i[1]) for i in case1]), sum([short(i[0],i[1]) for i in case2])) 
    
    print(ans if ans < inf else '-1')
       
