import heapq
import sys
inf = sys.maxsize
read = sys.stdin.readline


def short(s):
    
    distance = [inf for _ in range(n+1)]
    q = []
    heapq.heappush(q, (0,s))
    distance[s] = 0
    
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
           
    return distance


if __name__ == '__main__':
    
    T = int(input())
    
    for _ in range(T):
        
        n,m,t = map(int, read().split())    
        s,g,h = map(int, read().split())

        graph = [[] for _ in range(n+1)]

        for _ in range(m):
            a,b,d = map(int, read().split())
            graph[a].append((b,d))
            graph[b].append((a,d))

        candidate = [int(read().strip()) for _ in range(t)]
        
        ans=[]
        
        start_graph = short(s)
        g_graph = short(g)
        h_graph = short(h)  
        
        for end in candidate:           
            ANS1 = start_graph[g] + g_graph[h] + h_graph[end]
            ANS2 = start_graph[h] + h_graph[g] + g_graph[end]
            SHORT = start_graph[end] 
            
            if ANS1 == SHORT or ANS2 == SHORT:
                ans.append(end) ## 특정 길을 거치더라도 전체적으로 보았을 경우 목적지까지는 최단거리로 가야함
                
        ans = sorted(ans)
        for i in ans:
            print(i ,end=' ')    
    
