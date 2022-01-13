import sys
read = sys.stdin.readline

def cal(num, new_num):
    
    if (num == 0) or (num == 1):
        return num + new_num
    
    else:
        if (new_num == 0) or (new_num == 1):
            return num + new_num

        else: 
            return num * new_num

def solution(S):
        
    for idx, i in enumerate(S):
        if idx == 0:
            ans = i
        else:
            ans = cal(ans, i)
        
    print(ans)
        
if __name__ == "__main__":
    S = list(map(int, input()))
    solution(S)
