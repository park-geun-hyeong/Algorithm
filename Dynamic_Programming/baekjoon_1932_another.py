import sys
read = sys.stdin.readline

def solution(n, triangle):
    
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                left_up = 0
            else:
                left_up = triangle[i-1][j-1]
            
            if j == i:
                right_up = 0
            else:
                right_up = triangle[i-1][j]    
                
            triangle[i][j] = triangle[i][j] + max(left_up, right_up)
    
    ans = max(triangle[n-1])
    return ans

if __name__ == "__main__":
    n = int(read().rstrip())
    triangle = []
    for _ in range(n):
        row = list(map(int, read().split()))
        triangle.append(row)
        
    print(solution(n, triangle))
