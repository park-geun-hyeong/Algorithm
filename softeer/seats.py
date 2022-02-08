# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=625

import sys
import math
read = sys.stdin.readline

def cal_dist(one,two):
    x1,y1 = one
    x2,y2 = two
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def get_seat(graph, ID):
    
    n = len(graph)
    m = len(graph[0])
    if sum([sum(i) for i in graph]) == 0:
        return [0,0]
    
    can_seat = []
    not_seat = []
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]
    for row in range(n):
        for col in range(m):
            if graph[row][col] != 0:
                not_seat.append([row,col])
            else:
                can_seat.append([row,col])
            
    cand=[]
    for can in can_seat:
        row = can[0]
        col = can[1]
        possible = [0]*4
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if nrow<0 or nrow>=n or ncol<0 or ncol>=m:
                possible[i] = 1
            
            elif 0<=nrow<n and 0<=ncol<m and graph[nrow][ncol] == 0:
                possible[i] = 1
                                    
        if sum(possible) == 4:
            safety = 10e9
            for seated in not_seat:
                safety = min(safety, cal_dist(can,seated))

            cand.append([row,col,safety])
    
    if len(cand) == 0:
        return False
    return sorted(cand, key = lambda x : (-x[2], x[0], x[1]))[0][:2]
    
def solution(n,m,q,state):
    
    graph = [[0]*m for _ in range(n)]
    eat_check = [0] * 10001
    sitting_check = [0] * 10001
    loc = [0] * 10001
    ans = []
    for how, ID in state:
        ID = int(ID)
        if how == 'In':
            if sitting_check[ID] == 1:
                ans.append(f"{ID} already seated.")

            elif sitting_check[ID] == 0 and eat_check[ID] == 1:
                ans.append(f"{ID} already ate lunch.")
            
            elif sitting_check[ID] == 0 and eat_check[ID] == 0:
                try:
                    x,y = get_seat(graph,ID) 
                    loc[ID] = [x,y]
                    sitting_check[ID] = 1
                    eat_check[ID] = 1
                    graph[x][y] = ID
                    ans.append(f"{ID} gets the seat ({x+1}, {y+1}).")

                except TypeError:
                    ans.append("There are no more seats.")
        
        else:
            if eat_check[ID] == 0:
                ans.append(f"{ID} didn't eat lunch.")
            elif eat_check[ID] == 1 and sitting_check[ID] == 0:
                ans.append(f"{ID} already left seat.")
            elif eat_check[ID] == 1 and sitting_check[ID] == 1:
                x,y = loc[ID]
                ans.append(f"{ID} leaves from the seat ({x+1}, {y+1}).")
                sitting_check[ID] = 0
                graph[x][y] = 0

    return ans

if __name__ =="__main__":
    n,m,q = list(map(int, read().split()))
    state = [list(map(str, read().split())) for _ in range(q)]
    for i in solution(n,m,q,state):
        print(i)
