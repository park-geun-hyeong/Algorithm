import sys 
from itertools import permutations
read = sys.stdin.readline
# 총 연산은 n-1번 이루어져야함

def cal(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        if num1 >= 0:
            return num1 // num2
        else: 
            return -((-num1) // num2)
        
result = 0
def solution(Oper):
    
    ans = []
    global result
    
    for o in Oper:

        for idx, num in enumerate(seq):
            if idx == 0:
                result = num
            else: 
                result = cal(result, num, o[idx -1])
        ans.append(result)
        result = 0
              
    return ans

if __name__ == "__main__":
    n = int(input())
    seq = list(map(int, input().split()))
    operation = list(map(int, input().split()))
    oper=[]
    for idx, i in enumerate(operation):
        if idx == 0:
            oper.extend(['+'] * i)
        elif idx == 1:
            oper.extend(['-'] * i)
        elif idx == 2:
            oper.extend(['*'] * i)
        elif idx == 3:
            oper.extend(['/'] * i)
            
    Oper = list(permutations(oper, n-1)) 
    ans = solution(Oper)
    
    print(max(ans))
    print(min(ans))
    
    
    
    
