import sys
read = sys.stdin.readline 

def two_pointer(start, end, water):
    
    if (water[0]>0 and water[-1]>0):
        return 0,1
    elif (water[0]<0 and water[-1]<0):
        return -2,-1
    
    ans = abs(water[start] + water[end])
    ans_start = start
    ans_end = end
    while(start<end):  
        #print(water[start], water[end])
        now = water[start] + water[end]
        if abs(now) < ans:
            ans = abs(now)
            ans_start = start
            ans_end = end

        if now<0:
            start += 1
        elif now == 0:
            return start, end 
        else:
            end -= 1
        
    return ans_start, ans_end

if __name__ == "__main__":
    n = int(read().rstrip())
    water = list(map(int, read().split()))
    
    water.sort()
    start, end = two_pointer(0,n-1,water)    
    print(water[start], water[end])
    
