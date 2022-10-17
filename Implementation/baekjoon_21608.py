drow = [1,-1,0,0]
dcol = [0,0,1,-1]

def first(n, graph, now, like):
    global drow, dcol
    MAX=-1
    cases=[]
    for row in range(n):
        for col in range(n):
            if graph[row][col] == 0:
                check = 0
                for i in range(4):
                    nrow = row + drow[i]
                    ncol = col + dcol[i]
                    if 0<=nrow<n and 0<=ncol<n:
                        if graph[nrow][ncol] == 0:
                            continue
                        elif graph[nrow][ncol] in like:
                            check +=1
                cases.append([check, row, col])
    
    cases.sort(key = lambda x : -x[0])
    max_value = cases[0][0]
    idx = 0
    return_cases=[]
    while idx<len(cases):
        if cases[idx][0] == max_value:
            return_cases.append(cases[idx][1:])
            idx+=1
        else:
            break
    
    return return_cases
                    
def second(n, graph, cases):
    global drow, dcol
    return_cases=[]

    for i in range(len(cases)):
        row = cases[i][0]
        col = cases[i][1]
        check = 0
        for j in range(4):
            nrow = row + drow[j]
            ncol = col + dcol[j]
            if 0<=nrow<n and 0<=ncol<n:
                if graph[nrow][ncol] == 0:
                    check += 1
        
        return_cases.append([check, row, col]) 
    return_cases.sort(key = lambda x:(-x[0], x[1], x[2]) )
#     print(return_cases)
    return return_cases[0][1:]

def solution(n, student, seqence):
    global drow, dcol
    
    graph = [[0]*n for _ in range(n)]
    for idx, data in enumerate(sequence):
#         print("="*10)
#         for i in range(n):
#             for j in range(n):
#                 print(graph[i][j], end =" ")
#             print()
        now = data
        like = student[data]
        if idx == 0:
            graph[1][1] = data
            continue
        elif idx == n**2-1:
            for row in range(n):
                for col in range(n):
                    if graph[row][col] == 0:
                        graph[row][col] = data
                        break
                
            score = 0
            for row in range(n):
                for col in range(n):
                    now = graph[row][col]
                    check = 0
                    for i in range(4):
                        nrow = row + drow[i]
                        ncol = col + dcol[i]
                        if 0<=nrow<n and 0<=ncol<n:
                            if graph[nrow][ncol] in student[now]:
                                check+=1  
                    if check == 0:
                        continue
                    else:
                        score+=(10**(check-1))
            
            return score
        
        cases = first(n, graph, now, like)
        if len(cases) == 1:
            row = cases[0][0]
            col = cases[0][1]
            graph[row][col] = now
            continue
        else:
            cases = second(n, graph, cases)
            row = cases[0]
            col = cases[1]
            graph[row][col] = now
            continue
            
    return None

if __name__ == "__main__":
    n = int(input())
    student = [[0] for _ in range(n**2+1)]
    sequence = []
    for _ in range(n**2):
        info = list(map(int, input().split()))
        sequence.append(info[0])
        student[info[0]] = info[1:]
        
#     n = 3
#     sequence = [4,3,9,8,7,1,6,5,2]
#     student =[[],
#              [9,2,5,7],
#              [9,3,1,4],
#              [1,9,4,5],
#              [2,5,1,7],
#              [1,9,2,8],
#              [5,2,3,4],
#              [2,3,4,8],
#              [1,9,3,4],
#              [8,1,2,3]]
    ans = solution(n, student, sequence)
    print(ans)
