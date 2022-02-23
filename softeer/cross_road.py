import sys
from collections import deque, defaultdict
read = sys.stdin.readline

def zero():
    return 0 

def possible(i,cand):
    
    if i == 'A':
        if cand['D'] != 0:
            if cand['A'][1] ==  cand['D'][1]:
                return False
    
    if i == 'B':
        if cand['A'] != 0:
            if cand['B'][1] ==  cand['A'][1]:
                return False
    
    if i == 'C':
        if cand['B'] != 0:
            if cand['C'][1] ==  cand['B'][1]:
                return False

    if i == 'D':
        if cand['C'] != 0:
            if cand['D'][1] ==  cand['C'][1]:
                return False

    return True

def solution(n, state):
    
    ans = [-1]*n
    while True:
        road = ['A','B','C','D']
        cand = defaultdict(zero)
        
        check = 0
        for i in road:
            if len(state[i]) != 0:
                cand[i] = state[i].popleft()
                check += 1
        
        if check == 0:
            break
        
        
        if check == 4: 
            num = cand['A'][1]
            if cand['B'][1] == num and cand['C'][1] == num and cand['D'][1] == num:
                break
        
        
        time = min([cand[i][1] for i in road if cand[i] != 0])
        
        for i in road:
            
            if cand[i] == 0:
                continue
            
            if cand[i][1] != time:
                state[i].appendleft(cand[i])
                continue
                
            if cand[i][1] == time:
                if possible(i, cand) == True:
                    ans[cand[i][0]] = cand[i][1]
                
                else:
                    
                    if len(state[i]) != 0:
                        for idx, k in enumerate(state[i]):
                            if k[1] > cand[i][1]+1:
                                break

                            if k[1] == cand[i][1]+1:
                                state[i][idx][1] += 1

                    state[i].appendleft([cand[i][0], cand[i][1] + 1])
                    
        
    return ans

if __name__ == "__main__":
    
    n = int(read().rstrip())
    state = dict()
    for i in ['A','B','C','D']:
        state[i] = deque([])
        
    for i in range(n):
        t,w = map(str, read().split())
        state[w].append([i,int(t)])
        
    for i in solution(n,state):
        print(i)
