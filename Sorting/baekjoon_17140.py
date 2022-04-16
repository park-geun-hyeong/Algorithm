import sys
from collections import defaultdict
from itertools import chain
read = sys.stdin.readline

def transpose(A):
   
    r = len(A) 
    c = len(A[0])
           
    T_mat = [[0]*r for _ in range(c)]
    
    for i in range(c):
        for j in range(r):
            T_mat[i][j] = A[j][i] 
            
    return T_mat
    
def calculation(A):
    new_mat = [] 
    max_len = 0
    for row in A:
        new_row=[]
        nums = dict()
        for num in row:
            if num == 0:
                continue
            try:
                nums[num] += 1
            except KeyError:
                nums[num] = 1
         
        for a in nums.items():
            new_row.append(a)
        
        new_row = list(chain(*sorted(new_row, key = lambda x : (x[1], x[0]))))
        max_len = max(max_len, len(new_row))
        new_mat.append(new_row)
    
    new_mat = [row + [0] * (max_len - len(row)) if len(row)<max_len else row for row in new_mat]    
    return new_mat

def solution(r,c,k,A):
    time = 0

    while True:
        
        if time>100:
            return -1
        
        try:
            if A[r-1][c-1] == k:
                return time
        except:
            pass
        
        row_num = len(A)
        col_num = len(A[0])
        
        if row_num > 100:
            A = [i[:100] for i in A]
        
        if col_num > 100:
            A = transpose([i[:100] for i in transpose(A)])
            
            
        if row_num>=col_num:
            A = calculation(A)
        else:
            A = transpose(calculation(transpose(A)))
        
        time += 1
    return 
    
if __name__ == "__main__":
    r,c,k = map(int, read().split())
    A = [list(map(int, read().split())) for _ in range(3)]
    
    print(solution(r,c,k,A))
    
    
    
    
    
    
    
