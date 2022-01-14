import sys      
 
def solution(S):
    
    zero_cnt = 0
    one_cnt = 0
    
    for i in range(len(S)):
        if i == 0:
            if S[i] == '0':
                zero_cnt += 1
            else: 
                one_cnt += 1
        
        else:
            if S[i] != S[i-1]:
                if S[i] == '0':
                    zero_cnt += 1
                else:
                    one_cnt += 1
                    
    return min(zero_cnt, one_cnt)

if __name__ == "__main__":
    S = sys.stdin.readline().rstrip()
    assert len(S) <= int(1e6)
    
    print(solution(S)) 
