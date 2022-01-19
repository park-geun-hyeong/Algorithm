'''
# 나의 코드는 정확도 97%의 점수로 탈락했는데 어떤 예외가 있는지 다시 생각해보기

from copy import deepcopy

def rotation(m,key_out):
    # 시계방향 90도
    new_key=[]
    for i in key_out:
        row,col = i
        new_key.append([col, m-1-row])
        
    return new_key

def check(n,lock_padding):
    
    padding_length = len(lock_padding)
    for i in range(n-1, padding_length - (n-1)):
        for j in range(n-1, padding_length - (n-1)):
            if lock_padding[i][j] != 1:
                return False
    
    return True

def solution(key ,lock):
    m = len(key)
    n = len(lock)
    
    padding_length = m+(2*(n-1))
    lock_padding = [[1] * (padding_length) for _ in range(padding_length)]
    for i in range(m):
        for j in range(n):
            if lock[i][j] == 0:
                I = i+(n-1)
                J = j+(n-1)
                lock_padding[I][J] = 0
    
    key_out=[]
    for i in range(m):
        for j in range(m):
            if key[i][j] == 1:
                key_out.append([i,j])
     

    for _ in range(4):
        key_out = rotation(m,key_out)
        for i in range(padding_length - (n-1)):
            for j in range(padding_length - (n-1)):
                drow = i 
                dcol = j
                copy_padding_lock = deepcopy(lock_padding)
                for row, col in key_out:
                    nrow = drow + row
                    ncol = dcol + col
                    
                    copy_padding_lock[nrow][ncol] += 1
                
                if check(n, copy_padding_lock):
                    return True
                    
    return False
'''

def rotation(key):
    
    m = len(key)
    new_key=[[0]*m for _ in range(m)]
    for row in range(m):
        for col in range(m):
            new_key[col][m-1-row] = key[row][col]
    
    return new_key

def check(lock_padding):
    
    padding_length = len(lock_padding)
    n = padding_length // 3
    
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if lock_padding[i][j] != 1:
                return False
    
    return True

def solution(key ,lock):
    m = len(key)
    n = len(lock)
    
    padding_length = 3*n
    
    lock_padding = [[0] * padding_length for _ in range(padding_length)]
    for i in range(n):
        for j in range(n):
            lock_padding[i+n][j+n] = lock[i][j] 

    for _ in range(4):
        key = rotation(key)
        for drow in range(2*n):
            for dcol in range(2*n):
                for key_row in range(m):
                    for key_col in range(m):
                        nrow = key_row + drow
                        ncol = key_col + dcol
                        
                        lock_padding[nrow][ncol] += key[key_row][key_col]
                    
                if check(lock_padding):
                    return True
                
                ## padding lock 원상복귀
                for key_row in range(m):
                    for key_col in range(m):
                        nrow = key_row + drow
                        ncol = key_col + dcol
                        
                        lock_padding[nrow][ncol] -= key[key_row][key_col]
                                            
    return False
    
if __name__ == "__main__":
    key = [[0,0,0],[1,0,0],[0,1,1]]
    lock = [[1,1,1],[1,1,0],[1,0,1]]
    print(solution(key, lock))
