from bisect import bisect_left, bisect_right

def solution(x, num_list):
    left_idx = bisect_left(num_list, x)
    right_idx = bisect_right(num_list, x)
    
    return abs(right_idx - left_idx) 
       
    
if __name__ == "__main__":
    #n,x = list(map(int, input().split()))
    #num_list = list(map(int, input().split()))
    
    n = 7
    x = 2
    
    num_list= [1,1,2,2,2,2,3]
    print(solution(x,num_list))
    
