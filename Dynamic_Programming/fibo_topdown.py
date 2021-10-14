arr =  [0,1]

def fibo_dp(n):
    if n < len(arr):
        return arr[n]
    else:
        fibo = fibo_dp(n-1) + fibo_dp(n-2)
        arr.append(fibo)
        return fibo
if __name__ =='__main__':
    print(fibo_dp(10))
