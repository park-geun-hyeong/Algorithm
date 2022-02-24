# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=584&sw_prbl_sbms_sn=44255

import sys
read= sys.stdin.readline

def solution(n,m,restrict, test):
    
    state = [0 for _ in range(100)]
    
    start = 0
    for meter, speed in restrict:
        state[start: start + meter] = [speed] * meter 
        start = start + meter
        
    ans = []
    start = 0 
    for meter, speed in test:
        for i in range(start, start+meter):
            if speed - state[i] > 0: 
                ans.append(speed - state[i])
            
        start = start + meter
    if len(ans) == 0:
        return 0
    return max(ans)

if __name__ == "__main__":
    n,m = map(int, input().split())
    restrict = [list(map(int, read().split())) for _ in range(n)]
    test = [list(map(int, read().split())) for _ in range(m)]
    
    print(solution(n,m,restrict, test))
