import sys
import heapq
read = sys.stdin.readline
inf = sys.maxsize

def shortest_path(start, n,m,x):
    # start 노드에서 모든 노드까지의 최단거리 구하는 것이 목표
    global linked_list, paths
            
    paths[start][start] = 0
    q=[]
    heapq.heappush(q, [0, start])
        
    while q:
        current_dist, current_dst = heapq.heappop(q)
        
        if current_dist > paths[start][current_dst]:
            continue
            
        for new_dst, new_dist in linked_list[current_dst]:
            new = current_dist + new_dist # start->current_dst(link)->new_dst
            if new < paths[start][new_dst]:
                paths[start][new_dst] = new
                q.append([new, new_dst])
            
if __name__ == "__main__":
    
    n,m,x = map(int, read().split())
    linked_list = [[] for _ in range(n+1)]
    for i in range(1,m+1):
        s,e,t = map(int, read().split())
        linked_list[s].append([e,t])
        
    paths = [[inf]*(n+1) for _ in range(n+1)]
    #O(n*mlogn)
    for start in range(1, n+1):
        shortest_path(start,n,m,x)
    
    ans = max([paths[i][x] + paths[x][i] for i in range(1,n+1)])
    print(ans)
    
