#https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=414&sw_prbl_sbms_sn=43710
import sys
from collections import deque
read = sys.stdin.readline

def solution(n,k,robot):
       
    robot_loc = deque([]) 
    article = [0] * n
    if n == 1:
        return 0
    for i in range(n):
        if robot[i] == 'P':
            robot_loc.append(i)
            article[i] = 1
        
    idx = 0
    cnt = 0
    
    while robot_loc:
        idx = robot_loc.popleft()
        if k>=n:
            locs = range(0,n)
        else:
            if idx-k < 0:
                locs = range(0,idx+k+1)
            elif idx + k + 1 >= n:
                locs = range(idx-k, n)
            elif idx-k<0 and idx+k+1>=n:
                locs = range(0, n)
            else:
                locs = range(idx - k, idx + k + 1)
                
        for loc in locs:
            if article[loc] == 0:
                cnt += 1
                article[loc] = 1
                break
  
    return cnt
 
if __name__ == "__main__":
    n,k = list(map(int, read().split()))
    robot = list(map(str, read().rstrip()))
    print(solution(n,k,robot))

    
