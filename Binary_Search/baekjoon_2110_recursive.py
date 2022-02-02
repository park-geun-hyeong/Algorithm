import sys 
read = sys.stdin.readline

ans = 0
def bi_search(start,end, house,c):
    global ans
    if start > end:
        return ans 
    
    mid = (start + end) // 2
    cnt = 1
    value = house[0]
    for i in range(1, len(house)):
        if house[i]>=value + mid:
            value = house[i]
            cnt += 1
            
    if cnt>=c:
        ans = mid
        return bi_search(mid+1, end, house,c)
    else:
        return bi_search(start, mid-1, house, c)
 
if __name__ == "__main__":
    n,c = list(map(int, read().split()))
    house = [int(read().rstrip()) for _ in range(n)]
    
    house.sort()
    start = 1 
    end = house[-1] - house[0]
    
    Ans = bi_search(start, end, house, c)
    print(Ans)

