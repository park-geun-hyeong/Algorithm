import sys
read = sys.stdin.readline

def MovingCloud(cloud,graph,n, d, s):

    drow = [0,0,-1,-1,-1,0,1,1,1]
    dcol = [0,-1,-1,0,1,1,1,0,-1] 
    new_cloud = []
    cloud_graph = [[0]*n for _ in range(n)]
    for row, col in cloud:
#         cnt = 0
#         while True:
#             nrow = row + drow[d]
#             ncol = col + dcol[d]
            
#             if nrow > n-1:
#                 nrow = 0
#             elif nrow < 0:
#                 nrow = n-1
            
#             if ncol > n-1:
#                 ncol = 0
#             elif ncol < 0:
#                 ncol = n-1
                
#             cnt += 1
#             if cnt == s:
#                 break
#             row = nrow
#             col = ncol   
        nrow = (row + drow[d] * s)%n 
        ncol = (col + dcol[d] * s)%n
        
        new_cloud.append((nrow, ncol))
        cloud_graph[nrow][ncol] = 1
        graph[nrow][ncol] += 1

    return new_cloud, graph, cloud_graph

def copymagic(cloud, graph, n):
 
    diagonal_row = [1,1,-1,-1]
    diagonal_col = [1,-1,1,-1]
    
    for row,col in cloud:
        cnt = 0
        for i in range(4):
            nrow = row + diagonal_row[i]
            ncol = col + diagonal_col[i]
            if 0<=nrow<n and 0<=ncol<n:
                if graph[nrow][ncol] > 0:
                    cnt += 1 
        
        graph[row][col] += cnt     
    return graph

def solution(graph,cloud,n,m,move):
   
    cnt = 0
    for d, s in move:
        cloud, graph, cloud_graph = MovingCloud(cloud, graph,n,d,s)
        graph = copymagic(cloud, graph, n)
        new_cloud = [] 
        for row in range(n):
            for col in range(n):
                if cloud_graph[row][col] == 0 and graph[row][col] >= 2:
                    new_cloud.append((row,col))
                    graph[row][col] -= 2
        
        cloud = new_cloud
       
    return sum([sum(i) for i in graph])

if __name__ == "__main__":
    
    n,m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    move = [list(map(int, input().split())) for _ in range(m)]
    cloud = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
    
    ans = solution(graph,cloud,n,m,move)
    print(ans)
    
