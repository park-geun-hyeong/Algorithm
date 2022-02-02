import sys 
read = sys.stdin.readline

H=0
def bi_search(start, end, tree,m):
    global H
    
    if start > end:
        return H
    
    mid = (start+end) // 2
    residual = sum([i-mid if i>mid else 0 for i in tree])
    
    if residual < m:
        return bi_search(start, mid-1,tree,m)
    else:
        H = mid
        return bi_search(mid+1, end, tree, m)
    
    
if __name__ == "__main__":
    n,m = list(map(int,read().split()))
    tree = list(map(int, read().split()))
     
    start = 0
    end = max(tree)
    
    ans = bi_search(start, end, tree, m)
    print(ans)
    
