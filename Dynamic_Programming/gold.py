import sys 
read = sys.stdin.readline

def solution(n,m,graph):
        
    for col in range(1,m):
        for row in range(n):
            if row == 0:
                left_up = 0
            else: 
                left_up = graph[row-1][col-1]
                
            if row == n-1:
                left_down = 0
            else:
                left_down = graph[row+1][col-1]
                
            left = graph[row][col-1]
            
            graph[row][col] = graph[row][col] + max(left,left_up,left_down)

    ans = max([graph[i][m-1] for i in range(n)]) 
    return ans

if __name__ == "__main__":
    T = int(input())
    Ans = []
    for _ in range(T):
        n,m = list(map(int, read().split()))
        gold = list(map(int,read().split()))
        
        graph = []
        loc = 0
        for i in range(n):
            graph.append(gold[loc:loc+m])
            loc+=m

        Ans.append(solution(n,m,graph))
    
    for i in Ans:
        print(i)
        
                    
        
        
