'''
# brute force(time limit)

import sys
read = sys.stdin.readline

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    num = len(food_times)
    pivot = 0 
    cnt = 0
    
    while True:    
        
        if all(food_times) == False:
            return -1
        
        if pivot == num:
            pivot = 0
        
        if food_times[pivot] == 0:
            pivot += 1 
            continue
        else:
            if cnt == k:
                break            
            food_times[pivot] -= 1
            pivot += 1
            cnt+=1
                
    answer = pivot   
    return answer

if __name__ == "__main__":
    food_times = list(map(int, input().split()))
    k = int(input())
    print(solution(food_times, k))
    
'''

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    length = len(food_times)
    
    q=[]
    for i in range(length):
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0 # 총 시간 축적
    previous = 0 # 이전loop회전 수
    
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
        
    result = sorted(q, key= lambda x : x[1])
    answer = result[(k-sum_value) % length][1]
    
    return answer

if __name__ == "__main__":
    food_times = list(map(int, input().split()))
    k = int(input())
    print(solution(food_times, k))
    
