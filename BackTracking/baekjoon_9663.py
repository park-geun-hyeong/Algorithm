# back tracking = dfs + pruning
# DFS - 유망한 노드 검토 - 서브트리이동 - 백트래킹 수행
# n x n 행렬에 서로 공격하지 않도록 n개의 queen을 놓기 위해서는 각각의 행에 하나씩 위치시켜야함 

ans = 0
def N_queen(rowPos):
    global ans
    
    if rowPos == n:
        ans += 1 
        return 
    
    for col in range(n):
        flag = True
        
        for row in range(rowPos):
            if queen_loc[row] == col or rowPos - row == abs(col - queen_loc[row]):
                flag = False
                break
                
        if flag:
            queen_loc[rowPos] = col
            N_queen(rowPos + 1)
    
if __name__ == "__main__":
    n = int(input())
    assert 1<= n < 15

    queen_loc = [0] *n ## 배열의 i번째 요소의 값을 a라고 했을 경우 i행 a열에 퀸 존재한다는 뜻
    
    N_queen(0)
    print(ans)
    
