import heapq
import sys
read = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                    

if __name__ == "__main__":
    v,e = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(v+1)]
    distance = [INF for _ in range(v+1)]
    
    for _ in range(e):
        a,b,w = map(int, read().split())
        graph[a].append((b,w))
        
    
    dijkstra(start)
    
    for i in range(1, v+1):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])
    
    
