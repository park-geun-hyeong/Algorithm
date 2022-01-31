import sys
read = sys.stdin.readline
#https://programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    
    answer = []
    member_num = len(stages)
    
    for i in range(1,N+1):       
        stage_member = 0
        for j in stages:
            if j==i:
                stage_member +=1
            
        try:
            rate =  stage_member/member_num
        except ZeroDivisionError:
            rate = 0
                
        member_num -= stage_member
        answer.append((i, rate))
    
    ans = sorted(answer, key = lambda x: (-x[1], x[0]))
    new = [i[0] for i in ans]
        
    return new

if __name__ =="__main__":
    N1 = 5
    stages1 = [2,1,2,6,2,4,3,3]
    
    N2 = 4
    stages2 = [4,4,4,4,4]
    print(solution(N2, stages2))
