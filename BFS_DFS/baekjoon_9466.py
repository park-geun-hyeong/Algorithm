import sys
read = sys.stdin.readline
sys.setrecursionlimit(111111)

def dfs(i):
    global student, cnt, check,trace

    check[i] = 1
    trace.append(i)
    pick = student[i]
     
    if check[pick]:
        if pick in trace:
            cnt += len(trace[trace.index(pick):])
        return
    else:
        dfs(pick)            

if __name__ == "__main__":
    t = int(input())
    ans =[]
    for _ in range(t):
        cnt = 0
        n = int(input())
        student = [0] + list(map(int, read().split()))
        check = [0]*(n+1)
        
        for i in range(1,n+1):
            if check[i] == 0:
                if student[i] == i:
                    cnt += 1
                    check[i] = 1
                else:
                    trace = []
                    dfs(i)
                   
        ans.append(n-cnt)
    
    for i in ans:
        print(i)
