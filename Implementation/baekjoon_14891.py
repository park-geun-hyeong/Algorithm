import sys 
read = sys.stdin.readline
from collections import deque

state = [list(input()) for _ in range(4)]
k = int(input())
method = [list(map(int, input().split())) for _ in range(k)]
state = [list(map(int, i)) for i in state]

def move(direction, row):
    ans = [0]*8
    
    if direction == 1:
        for i in range(1,9):
            ans[i%8] =row[i-1]
    else:
        for i in range(1,9):
            ans[i-1] = row[i%8]
    return ans
    
# 맞닿은 톱니의 극이 같다 -> 회전하지 않는다.
# 맞닿은 톱니의 극이 다르다 -> 옆에 친구 반대방향 회전

def find(gear):
    if gear == 0:
        return [[[gear,2], [gear+1, 6]]]
    
    elif gear == 3:
        return [[[gear,6], [gear-1, 2]]]
    
    else:
        return [[[gear,6], [gear-1, 2]], [[gear,2], [gear+1, 6]]]
         
def opp(direction):
    if direction == 1:
        return -1
    else:
        return 1

def solution():
    
    global state
     
    for gear, direction in method: 
        order = [[0]*2 for _ in range(4)]
        order[gear-1][0] = 1
        order[gear-1][1] = direction
        visit = [0]*4
        q = deque([[gear-1,direction]])
        
        while q:
            num, d = q.popleft()
            visit[num] = 1
            
            for A,B in find(num):
                me, my_loc = A
                you, your_loc = B
                
                if visit[you] == 0:
                    if state[me][my_loc] == state[you][your_loc]:
                        visit[you] = 1
                        continue 
                    
                    else:
                        order[you][0] = 1
                        order[you][1] = opp(d)
                        q.append([you, opp(d)])
                        
        for i in range(4):
            if order[i][0] == 1:
                state[i] = move(order[i][1], state[i])
       
    score = 0
    for i in range(4):
        if state[i][0] ==  0:
            continue
        elif state[i][0] == 1:
            score += (2**i)

    print(score)

solution()
