import sys
read= sys.stdin.readline

def check_row(i, row):
    for j in range(9):
        if i == graph[row][j]:
            return False
    return True

def check_col(i,col):
    for j in range(9):
        if i == graph[j][col]:
            return False
    return True

def check_square(i, row, col):
    nrow = (row // 3) * 3
    ncol = (col // 3) * 3
    
    for k in range(3):
        for j in range(3):
            if i == graph[nrow + k][ncol + j]:
                return False
    return True

state = False
def dfs(idx):
    
    global state
    
    if state:
        return
    
    if idx == len(zero_position):
        for i in graph:
            print(' '.join(map(str, i)))
            state = True
        return 
        
    for i in range(1, 10):
        row, col = zero_position[idx]
        if check_row(i,row) and check_col(i,col) and check_square(i,row,col):
            graph[row][col] = i
            dfs(idx + 1)
            graph[row][col] = 0 # 재귀안에서 답이 없을경우 초기화 한 뒤 다음 interation으로
            
if __name__ == "__main__":
    
    graph = [list(map(int, read().split())) for _ in range(9)]           
    zero_position = []
    for i in range(9):
        for j in range(9):
            if graph[i][j] == 0:
                zero_position.append([i,j])
    dfs(0)
