import sys 
read  = sys.stdin.readline

def rotation(key_out):
    # 시계방향 90도
    new_key=[]
    for i in key_out:
        row,col = i
        new_key.append([col, m-1-row])
        
    return new_key

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
                
    
    lp1 = lock_padding.copy()         
    for i in range(padding_length - (n-1)):
        for j in range(padding_length - (n-1)):
            drow = i
            dcol = j
            for row, col in key_out:
                nrow = drow + row
                ncol = dcol + col
                
                if (n-1<= nrow < padding_length-(n-1)) and (n-1<= ncol < padding_length-(n-1)) and lp1[nrow][ncol] == 1:
                     break
                    
                lp1[nrow][ncol] += 1
            if sum([sum(lp1[i][n-1: padding_length-(n-1)]) for i in range(n-1, padding_length-(n-1))]) == n**2:
                return True
            
    key_out = rotation(key_out)
    lp2 = lock_padding.copy()         
    for i in range(padding_length - (n-1)):
        for j in range(padding_length - (n-1)):
            drow = i
            dcol = j
            for row, col in key_out:
                nrow = drow + row
                ncol = dcol + col
                
                if (n-1<= nrow < padding_length-(n-1)) and (n-1<= ncol < padding_length-(n-1)) and lp2[nrow][ncol] == 1:
                     break
                    
                lp2[nrow][ncol] += 1
            if sum([sum(lp2[i][n-1: padding_length-(n-1)]) for i in range(n-1, padding_length-(n-1))]) == n**2:
                return True
    
    key_out = rotation(key_out)
    lp3 = lock_padding.copy()         
    for i in range(padding_length - (n-1)):
        for j in range(padding_length - (n-1)):
            drow = i
            dcol = j
            for row, col in key_out:
                nrow = drow + row
                ncol = dcol + col
                
                if (n-1<= nrow < padding_length-(n-1)) and (n-1<= ncol < padding_length-(n-1)) and lp3[nrow][ncol] == 1:
                     break
                    
                lp3[nrow][ncol] += 1
            if sum([sum(lp3[i][n-1: padding_length-(n-1)]) for i in range(n-1, padding_length-(n-1))]) == n**2:
                return True
            
    key_out = rotation(key_out)
    lp4 = lock_padding.copy()         
    for i in range(padding_length - (n-1)):
        for j in range(padding_length - (n-1)):
            drow = i
            dcol = j
            for row, col in key_out:
                nrow = drow + row
                ncol = dcol + col
                
                if (n-1<= nrow < padding_length-(n-1)) and (n-1<= ncol < padding_length-(n-1)) and lp4[nrow][ncol] == 1:
                     break
                    
                lp4[nrow][ncol] += 1
            if sum([sum(lp4[i][n-1: padding_length-(n-1)]) for i in range(n-1, padding_length-(n-1))]) == n**2:
                return True              
             
    return False
    
if __name__ == "__main__":
    key = [[0,0,0],[1,0,0],[0,1,1]]
    lock = [[1,1,1],[1,1,0],[1,0,1]]
    print(solution(key, lock))
