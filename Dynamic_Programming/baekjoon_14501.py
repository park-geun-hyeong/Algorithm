import sys
read = sys.stdin.readline

def possible(time_sheet,day):
    n= len(time_sheet)
    t,p = time_sheet[day]
    if day+t>n:
        return False
    return True
    

def solution(n, time_sheet):
    
    # i 일에 일을 했다고 가정하에 벌수 있는 최대의 돈
    # 일을 못할경우 벌 수 있는 돈은 0원이다.
    for i in range(n):
        oridinal = time_sheet[i][1]
        if possible(time_sheet, i):
            for j in range(i):
                t, p = time_sheet[j]
                if j + t <= i:
                    time_sheet[i][1] = max(oridinal + p, time_sheet[i][1])
                          
        else:
            time_sheet[i][1] = 0
    #print(time_sheet)       
    return sorted(time_sheet, key= lambda x : -x[1])[0][1]

if __name__ == "__main__":
    n = int(input())
    time_sheet = [list(map(int, input().split())) for _ in range(n)]
    
    print(solution(n, time_sheet))
    
   
