import sys
read = sys.stdin.readline

def change(direction):
    if direction % 2 == 0:
        return direction - 1
    return direction + 1
    
def move(r,c,graph):
    
    drow = [0,-1,1,0,0]
    dcol = [0,0,0,1,-1]
    new_graph = [[0]*c for _ in range(r)]
    
    for row in range(r):
        for col in range(c):
            if graph[row][col] != 0:
                speed, direction, size = graph[row][col]
                cnt = 0
                pivot_row = row
                pivot_col = col
                while True:
                    if cnt == speed:
                        break
                        
                    nrow = pivot_row + drow[direction] 
                    ncol = pivot_col + dcol[direction] 
                    
                    if 0<=nrow<r and 0<=ncol<c:
                        cnt += 1
                        pivot_row = nrow
                        pivot_col = ncol
                        continue
                        
                    else: 
                        direction = change(direction)
                        pivot_row = pivot_row + drow[direction] 
                        pivot_col = pivot_col + dcol[direction] 
                        cnt += 1
                graph[row][col][1] = direction
                        
                if new_graph[pivot_row][pivot_col] == 0:
                    new_graph[pivot_row][pivot_col] = graph[row][col]
                else:
                    if new_graph[pivot_row][pivot_col][2] < size:
                        new_graph[pivot_row][pivot_col] = graph[row][col]

    return new_graph

def catch(loc, r, graph):
    
    size = 0
    for row in range(r):
        if graph[row][loc] != 0:
            size = graph[row][loc][2]
            graph[row][loc] = 0
            break
    
    return graph, size

def solution(r,c,m,graph):
    
    SUM = 0
    for loc in range(c):
        graph, size = catch(loc,r,graph)
        SUM += size
        graph = move(r,c,graph)
#         for i in graph:
#             print(i)
#         print("="*10)
                
    return SUM

if __name__ == "__main__":
    r,c,m = map(int, read().split())
    graph = [[0]*c for _ in range(r)]
    #mat = [[4, 1, 3, 3, 8],[1, 3, 5, 2, 9],[2, 4, 8, 4, 1],[4, 5, 0, 1, 4],[3, 3, 1, 2, 7],[1, 5, 8, 4, 3],[3, 6, 2, 1, 2],[2, 2, 2, 3, 5]]
    for _ in range(m):
        R,C,s,d,z, = map(int, read().split())
        #R,C,s,d,z, = mat[_]
        graph[R-1][C-1] = [s,d,z]
    
    ans = solution(r,c,m,graph)
    print(ans)
