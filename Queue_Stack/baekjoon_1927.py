import heapq
import sys

def solution(x):    
    
    arr=[]
    for i in x:
        if i>0:
            heapq.heappush(arr, i)
               
        else:
            try:
                print(heapq.heappop(arr))
            except IndexError:
                print('0')
            

if __name__ == '__main__':
    n = int(input())  
    x = [int(sys.stdin.readline()) for _ in range(n)]    
    solution(x)
    
    
