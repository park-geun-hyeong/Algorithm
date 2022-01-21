def point_change(n,x,y):
    return (n-y, x)

def point_change2(n,row, col):
    return (col, n-row)
    
def verticle_check(graph, b,  x, y):
    
    n = len(graph) - 1
    row,col = point_change(n,x,y)
    
    
    if b == 1:
        if y == 0  or graph[row+1][col] == 1 or graph[row][col-1] == 2 or graph[row-1][col-1] == 2: 
            return True
        
        elif row<1 or col<0 or col>n:
            return False
            
               
    else:
        if graph[row-1][col] == 2 and graph[row-1][col-1] == 2:
            return True
              
        elif graph[row-1][col] == 2 or graph[row-1][col] == 1:
            return False
        
        else:
            return True


def horizontal_check(graph, b, x, y):
    
    n = len(graph) - 1
    row,col = point_change(n,x,y)
    
    if b == 1:
        if  y == 0 or col >= n:
            return False
        
        else:
            if graph[row+1][col] == 1 or graph[row+1][col+1] == 1 or (graph[row][col+1] == 2 and graph[row][col-1] == 2):
                return True
        
    else:
        if graph[row][col+1] == 1 or (graph[row][col-1]==2 and graph[row][col+1] == 2):
            return False
        else:
            return True
        
def solution(n, build_frame):
    
    graph = [[0]*(n+1) for _ in range(n+1)]
    result = []
    
    for x,y,a,b in build_frame:
        if a==0:
            if verticle_check(graph, b, x, y):
                row,col = point_change(n,x,y)
                if b==1:
                    graph[row][col] += 1
                else:
                    graph[row][col] -= 1
                    
        else:
            if horizontal_check(graph,b,x,y):
                row,col = point_change(n,x,y)
                if b==1:
                    graph[row][col] += 2
                else:
                    graph[row][col] -= 2
       
    for i in range(n+1):
        for j in range(n+1):
            if graph[i][j] == 1:
                x,y = point_change2(n,i,j)
                result.append([x,y,0])
            elif graph[i][j] == 2:
                x,y = point_change2(n,i,j)
                result.append([x,y,1])
            
    return sorted(result) 


if __name__ == "__main__":
    n = 5
    build_frame1 = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    build_frame2 = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
    print(solution(n,build_frame1))
    
