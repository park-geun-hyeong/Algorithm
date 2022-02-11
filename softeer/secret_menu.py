# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=623&sw_prbl_sbms_sn=43650

import sys
read = sys.stdin.readline

def solution(secret_but, user_but):
    m = len(secret_but)
    n = len(user_but)
    
    if n<m:
        return 'normal'
    
    for i in range(n-m+1):
        window = user_but[i:i+m]
        if window == secret_but:
            return 'secret'
    
    return 'normal'

if __name__ == "__main__":
    m,n,k = list(map(int, read().split()))
    secret_but = list(map(int, read().split()))
    user_but = list(map(int, read().split()))
    
    print(solution(secret_but, user_but))
    
    
