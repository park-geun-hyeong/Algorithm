from collections import deque
import sys
read = sys.stdin.readline


def make_temp(state, head):
    
    if state == 1:
        return [head[0], head[1] + 1]
    elif state == 2:
        return [head[0] + 1, head[1]]
    elif state == 3:
        return [head[0], head[1] - 1]
    elif state == 4:
        return [head[0] - 1 , head[1]]
    
def State(state, snake, time):
    
    if snake[time] == "D":
            state += 1 
            if state == 5:
                state = 1
            
    elif snake[time] == "L":
        state -= 1
        if state == 0:
            state = 4
    
    return state
    
def game_over(n, snake_loc, temp):
    
    row, col = temp
    
    if row<1 or row>n or col<1 or col>n:
        return True
    
    if temp in snake_loc:
        return True
    
    return False

def solution(graph, snake):
    
    n = len(graph) - 1 
    state = 1
    time = 0
    snake_loc = deque([])
    snake_loc.append([1,1])
       
    while True:  
        time += 1
        head = snake_loc[0]
        temp = make_temp(state, head)
        
        if game_over(n, snake_loc, temp) == True:
            print(time)
            return None
        
        if graph[temp[0]][temp[1]] == 0:
            snake_loc.appendleft(temp)
            snake_loc.pop()
        else:
            graph[temp[0]][temp[1]] = 0
            snake_loc.appendleft(temp)
         
        state = State(state, snake, time)


if __name__ == "__main__":
    N = int(input())
    K = int(input()) 
    graph = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(K):
        row, col = list(map(int, read().split()))
        graph[row][col] = 1
        
    L = int(input())
    snake = [0] * 10001
    for _ in range(L):
        X,C = list(map(str ,read().split()))
        snake[int(X)] = C
    
    solution(graph, snake)
