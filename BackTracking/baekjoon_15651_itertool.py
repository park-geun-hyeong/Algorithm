from itertools import product

def permute(n,m):   
    return list(product(*([tuple(range(1,n+1))] * m)))
    
if __name__ == "__main__":
    n,m = tuple(map(int, input().split()))
    for i in permute(n,m):
        if m>1:
            for j in i:
                print(j, end=' ')
            print()
        else:  
            print(i[0])
        
    
    
