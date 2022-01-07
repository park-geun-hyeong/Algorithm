from itertools import combinations

def combinate(n,m):
    return list(combinations(range(1, n+1), m))
    
if __name__ == "__main__":
    n,m = tuple(map(int, input().split()))
    for i in combinate(n,m):
        if m>1:
            for j in i:
                print(j, end=' ')
            print()
        else:  
            print(i[0])
        
    
    
