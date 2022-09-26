from collections import deque
info = dict()

def init():
    global info
    info["direction"] = 1
    info['row'] = 0
    info['col'] = 0
    
    info['bottom'] = 6
    info['top'] = 1
    info['left'] = 4
    info['right'] = 3
    info['front'] = 2
    info['back'] = 5
    
    return 

def possible(target_row, target_col):
    if 0<=target_row<n and 0<=target_col<m:
        return True
    return False

def diceRolling(direction):
    global info
    bottom_ord = info['bottom']
    top_ord = info['top']
    left_ord = info['left']
    right_ord = info['right']
    front_ord = info['front']
    back_ord = info['back']
    
    if direction == 0:
        info['bottom'] = front_ord
        info['front'] = top_ord
        info['top'] = back_ord
        info['back'] = bottom_ord
        
    elif direction == 1:
        info['bottom'] = right_ord
        info['left'] = bottom_ord
        info['top'] = left_ord
        info['right'] = top_ord
    
    elif direction == 2:
        info['bottom'] = back_ord
        info['front'] = bottom_ord
        info['top'] = front_ord
        info['back'] = top_ord
                    
    elif direction == 3:
        info['bottom'] = left_ord
        info['left'] = top_ord
        info['top'] = right_ord
        info['right'] = bottom_ord    
    
    return 

def moving(graph):
    global info
    '''
    "direction"
    
    0: North
    1: East
    2: South
    3: West
    '''
    row = info['row']
    col = info['col']
    direction = info['direction']
    
    target_row, target_col, target_direction = 0, 0, 0
    if direction == 0:
        target_row = row-1
        target_col = col
        if not possible(target_row, target_col):
            target_row = row+1
            target_col = col
            direction = 2
         
    elif direction == 1: 
        target_row = row
        target_col = col+1
        if not possible(target_row, target_col):
            target_row = row
            target_col = col-1
            direction = 3
    
    elif direction == 2:
        target_row = row+1
        target_col = col
        if not possible(target_row, target_col):
            target_row = row-1
            target_col = col
            direction = 0

    elif direction == 3:
        target_row = row
        target_col = col-1
        if not possible(target_row, target_col):
            target_row = row 
            target_col = col+1
            direction = 1
    
    diceRolling(direction)
    
    target_score = graph[target_row][target_col]
    if info['bottom'] == target_score:
        target_direction = direction
    elif info['bottom'] > target_score:
        target_direction = (direction + 1)%4
    elif info['bottom'] < target_score:
        target_direction = (direction-1)
        if target_direction < 0:
            target_direction = 3
    
    info['row'] = target_row
    info['col'] = target_col
    info['direction'] = target_direction
     
    return 

def solution(n,m,k,graph):
    global info
    init()
    
    score = 0
    drow = [1,-1, 0, 0]
    dcol = [0, 0, 1, -1]

    for _ in range(k):
        cnt = 1
        moving(graph)
        target_score = graph[info['row']][info['col']]
        check = [[0]*m for _ in range(n)]
        
        q = deque([[info['row'], info['col']]])
        check[info['row']][info['col']] = 1
        while q:
            
            row, col = q.popleft()
            # print("row: {}, col:{} \n".format(row, col))
            
            for i in range(4):
                nrow = row + drow[i]
                ncol = col + dcol[i]
                if 0<=nrow<n and 0<=ncol<m:
                    if graph[nrow][ncol] == target_score and check[nrow][ncol] == 0:
                        q.append([nrow, ncol])
                        check[nrow][ncol] = 1
                        cnt += 1            
            
        score += (cnt * target_score)
    
    return score

if __name__ == "__main__":
    n,m,k = list(map(int,input().split()))
    graph = [list(map(int, input().split())) for _ in range(n)]
    # sample_graph =[[4,1,2,3,3],[6,1,1,3,3],[5,6,1,3,2],[5,5,6,5,5]]
    
    
    ans = solution(n,m,k,graph)
    print(ans)
