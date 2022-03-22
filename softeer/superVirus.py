mport sys
read = sys.stdin.readline

def recursive(p,n):  
    if n>1:
        if n%2 == 0:
            return (recursive(p,n//2) ** 2)%1000000007
        elif n%2 == 1:
            return (p*recursive(p,n//2)**2)%1000000007
    elif n == 1:
        return p%1000000007  
    return 
   

if __name__ == "__main__":
    k,p,n = map(int, read().split())
    num = (recursive(p, n*10))
    print((k*num)%1000000007)
