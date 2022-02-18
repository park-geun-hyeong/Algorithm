# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=407&sw_prbl_sbms_sn=43871 


import sys
read = sys.stdin.readline

def solution(k,p,n):
    
    cnt = 0
    num = k
    while True:
        num *= p
        cnt += 1
        if num > 1000000007:
            num %= 1000000007
        
        if cnt == n:
            break
        
    return num

if __name__ == "__main__":
    k,p,n = map(int,read().split())
    print(solution(k,p,n))
    
    
    
