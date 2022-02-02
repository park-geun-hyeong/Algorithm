
def bisearch(array, start, end):
    mid = (start + end) // 2
    
    if start>end:
        return -1
    
    if array[mid] == mid:
        return mid
    
    elif array[mid] < mid:
        return bisearch(array, mid+1, end)
    
    elif array[mid] > mid:
        return bisearch(array, start, end-1)
        
if __name__ == "__main__":
    n= int(input())
    array = list(map(int, input().split()))
    print(bisearch(array, 0, n-1))
    
    
