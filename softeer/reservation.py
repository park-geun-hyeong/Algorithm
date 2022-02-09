# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=626

import sys
from collections import defaultdict
read = sys.stdin.readline

def solution(name ,time):

    name.sort()
    T = defaultdict()
    for i in name:
        T[i] = [0]*24
     
    for name ,start ,end in time:
        start = int(start)
        end = int(end)
        T[name][start:end] = [1]*(end-start)
        
    ans = []
    for idx, (key, value) in enumerate(T.items()):
        ans.append(f"Room {key}:")
        if sum(value[9:18]) == 9:
            ans.append("Not available")
            if idx != n-1:
                ans.append('-'*5)
            continue

        part = []
        start = 9
        end = 10
        while True:
            if value[start] == 1:
                start += 1
                if start >= 18:
                    break
                end = start + 1
                continue
                
                
            if value[start] == 0:
                if value[end] == 0:
                    end += 1
                    if end > 18:
                        part.append([start, 18])
                        break

                else:
                    part.append([start,end])
                    start = end
        
        length = len(part)
        ans.append(f"{length} available:")
        for start, end in part:
            if start<10:
                start = f"0{start}"
            if end<10:
                end = f"0{end}"
            ans.append(f"{start}-{end}")
        
        if idx != n-1:
            ans.append('-'*5)
            
    return ans
        
if __name__ == "__main__":
    n,m = list(map(int,read().split()))
    name = [str(read().rstrip()) for _ in range(n)]
    time = [list(map(str, read().split())) for _ in range(m)]
    
    for i in solution(name, time):
        print(i)
    
