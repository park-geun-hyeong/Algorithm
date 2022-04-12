import sys
read = sys.stdin.readline

def prime_num(n):
    check = [True] * (n+1)
    check[0] = False
    check[1] = False
    
    for i in range(2, n+1):
        
        if check[i] == True:
            j = 2
            while(i*j<=n):
                check[i*j] = False
                j += 1
    
    return [i for i in range(n+1) if check[i]]
    
def solution(n):
    cnt = 0
    start = 0
    end = 0
    
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    
    nums = prime_num(n)
    #print(nums)
    part_sum = nums[0]
        
    while(start<=end):
        
        try:
            if part_sum == n:
                #print(start, end)
                cnt += 1
                end += 1
                part_sum += nums[end]

            if part_sum < n:
                end += 1
                part_sum += nums[end]
        
            elif part_sum > n:
                part_sum -= nums[start]
                start += 1
        except IndexError:
            break
    
    return cnt

if __name__ == "__main__":
    n = int(input())
    print(solution(n))
    
    
    
    
