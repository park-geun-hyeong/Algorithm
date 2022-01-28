import sys
from collections import deque

def get_next_loc(board, robot_loc):    
    next_loc = []
    n = len(board)
    
    one_row = list(robot_loc)[0][0]
    one_col = list(robot_loc)[0][1]
    two_row = list(robot_loc)[1][0]
    two_col = list(robot_loc)[1][1]

    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]
    
    # translation check
    for i in range(4):
        none_row = one_row + drow[i]
        none_col = one_col + dcol[i]
        ntwo_row = two_row + drow[i]
        ntwo_col = two_col + dcol[i]
        
        if 0<=none_row<n and 0<=none_col<n and 0<=ntwo_row<n and 0<=ntwo_col<n:
            if board[none_row][none_col] == 0 and board[ntwo_row][ntwo_col] == 0:
                next_loc.append({(none_row, none_col), (ntwo_row, ntwo_col)})
                               
    
    # Rotation check
    if one_row == two_row: # horizontal state
        # 1. horizontal state -> vertical below
        # 2. horizontal state -> vertical above
        for i in [1,-1]:
            if 0 <= one_row + i < n:
                if board[one_row+i][one_col] == 0 and board[two_row+i][two_col] == 0:
                    next_loc.append({(one_row, one_col), (one_row+i, one_col)})
                    next_loc.append({(two_row, two_col),(two_row+i, two_col)})

    elif one_col == two_col: # verticle state
        # 3. verticle state -> horizontal right
        # 4. verticle state -> horizontal left
        for i in [1,-1]:
            if 0<= one_col+i<n:
                if board[one_row][one_col+i] ==0 and board[two_row][two_col+i] == 0:
                    next_loc.append({(one_row,one_col), (one_row, one_col+i)})
                    next_loc.append({(two_row,two_col), (two_row, two_col+i)})
    
    return next_loc

def solution(board):
    n= len(board)
    q = deque()
    visited = [{(0,0),(0,1)}]
    
    q.append([{(0,0),(0,1)}, 0])
    target = (n-1,n-1)
    while q:
        loc, time = q.popleft()
        if target in loc:
            return time
        
        next_locs = get_next_loc(board, loc)
        for next_loc in next_locs:
            if next_loc not in visited:
                q.append([next_loc, time+1])
                visited.append(next_loc)
            
if __name__ == "__main__":
    board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
    print(solution(board))
