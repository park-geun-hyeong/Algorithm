def fibo_bottomup(n):
    if n==0:
        return 0
    elif n==1:
        return 1

    arr = [0,1]

    for i in range(2, n+1):
        fibo = arr[i-1]+arr[i-2]
        arr.append(fibo)

    return arr[n]

if __name__ =="__main__":
    print(fibo_bottomup(10))
