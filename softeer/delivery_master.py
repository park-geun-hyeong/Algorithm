#https://softeer.ai/practice/result.do?eventIdx=1&submissionSn=SW_PRBL_SBMS_43651&psProblemId=581

import sys
from itertools import permutations
read = sys.stdin.readline

def solution(n,m,k,weight):
    cases = list(permutations(weight))
    ans = []
    
    for case in cases:
        cnt = 0
        Sum = 0
        final = 0
        idx = 0
        
        while True:
            loc = idx % n
            if Sum + case[loc] > m:
                final += Sum
                Sum = case[loc]
                cnt += 1
                idx += 1
                if cnt == k:
                    break
            else:
                Sum += case[loc]
                idx += 1
        ans.append(final)   
          
    return min(ans)
    
if __name__ == "__main__":
    n,m,k = list(map(int, read().split()))
    weight = list(map(int, read().split()))
    
    print(solution(n,m,k,weight))
