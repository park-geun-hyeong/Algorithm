import sys
read = sys.stdin.readline

def next_dice(dice,i):
    if i == 1:
        dice[1],dice[3],dice[4],dice[6] = dice[4], dice[1],dice[6], dice[3]
    if i == 2:
        dice[1],dice[3],dice[4],dice[6] = dice[3], dice[6], dice[1], dice[4]
    if i == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    if i == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1],dice[6], dice[2]
        
    return dice

def solution(n,m,row,col,k,graph,order):
        
    dice = [0]*7
    
    drow = [0,0,0,-1,1] 
    dcol = [0,1,-1,0,0]
    
    ans = []
    for i in order:
        nrow = row + drow[i]
        ncol = col + dcol[i]
        if(0<=nrow<n and 0<=ncol<m):
            dice = next_dice(dice, i)

            if(graph[nrow][ncol] == 0):
                graph[nrow][ncol] = dice[6]            
            else:
                dice[6] = graph[nrow][ncol]
                graph[nrow][ncol] = 0

            ans.append(dice[1])
            row = nrow
            col = ncol

    return ans


if __name__ == "__main__":
    n,m,x,y,k = map(int, read().split())
    graph = [list(map(int, read().split())) for _ in range(n)]
    order = list(map(int, read().split()))
    
    for i in solution(n,m,x,y,k,graph,order):
        print(i)
    
    
    
    
