import sys
from collections import deque
read = sys.stdin.readline

def possible(i, same_time):
    
    if isinstance(same_time[0], tuple):
        same_time = [i[2] for i in same_time]
    
    if i == 'A':
        if 'D' in same_time:
            return False
    
    if i == 'B':
        if 'A' in same_time:
            return False
    
    if i == 'C':
        if 'B' in same_time:
            return False

    if i == 'D':
        if 'C' in same_time:
            return False

    return True 

def no_move(same_time):
    if isinstance(same_time[0], tuple):
        same_time = [i[2] for i in same_time]
    
    if 'A' in same_time and 'B' in same_time and 'C' in same_time and 'D' in same_time:
        return True
    return False
    

def solution(n, car):

    Car = deque([[idx, int(data[0]), data[1]] for idx, data in enumerate(car)])
    ans = [0] * n  
    ck = [0] * n
    same_time = deque([])
    
    idx, before_t, before_w = Car.popleft()
    same_time.append((idx, before_t, before_w))
    
    while Car:
        
        idx, now_t,now_w = Car.popleft()
        
        if len(same_time) == 0:
            same_time.append((idx, now_t, now_w))
            before_t = now_t
            continue
                        
        if now_t == before_t:
            same_time.append((idx, now_t, now_w))  
            continue
            
        if now_t != before_t:
            Car.appendleft([idx, now_t, now_w])
            
            if no_move(same_time):
                return [ans[i] if ck[i] == 1 else -1 for i in range(len(ck))]
            
            check = {'A':0, 'B':0,'C':0,'D':0} 
            only_w = [i[2] for i in same_time]
            for idx, t, w in same_time:
                
                if possible(w, only_w) and check[w] == 0:
                    ans[idx] = before_t
                    ck[idx] = 1
                    check[w] = 1
                else:
                    Car.appendleft([idx, t + 1, w])
            
            same_time = deque([])
    
    
    if len(same_time) > 0 :
        if no_move(same_time):
            return [ans[i] if ck[i] == 1 else -1 for i in range(len(ck))]
        
        only_w = [i[2] for i in same_time] 
        check = {'A':0, 'B':0,'C':0,'D':0}
        while same_time:
            
            idx, t, w = same_time.popleft()
            if t > before_t:
                before_t = t
                only_w = [i[2] for i in same_time]
                if len(only_w) == 0:
                    ans[idx] = before_t
                    break
                check = {'A':0, 'B':0,'C':0,'D':0}
            elif t == before_t:       
                if possible(w, only_w) and check[w] == 0:
                    ans[idx] = before_t
                    ck[idx] = 1
                    check[w] = 1

                else:
                    same_time.append((idx, before_t+1 ,w))   

    return ans

if __name__ == "__main__":
    n = int(input())
    car = [list(map(str, input().split())) for _ in range(n)]
    for i in solution(n,car):
        print(i)
    
