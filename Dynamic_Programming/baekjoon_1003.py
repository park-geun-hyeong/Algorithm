def solution(n):
    zero_num = [1,0]
    one_num = [0,1]
    
    for i in range(2, n+1):
        zero_num.append(zero_num[i-1] + zero_num[i-2])
        one_num.append(one_num[i-1] + one_num[i-2])
        
    
    return f"{zero_num[n]} {one_num[n]}"

if __name__ == "__main__":
    n = int(input())
    case = [int(input()) for _ in range(n)]
    for i in case:
        print(solution(i))

