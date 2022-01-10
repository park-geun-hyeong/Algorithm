import sys 
read = sys.stdin.readline

def dfs(num, idx, plus, sub, mul,div):
    global MAX, MIN
    
    if idx == n:
        MAX = max(MAX, num)
        MIN = min(MIN, num)
        return
    
    if plus > 0:
        dfs(num + seq[idx], idx + 1 ,plus -1, sub, mul, div)
    if sub > 0:
        dfs(num - seq[idx], idx +1 ,plus, sub-1, mul, div)
    if mul > 0:
        dfs(num * seq[idx], idx +1 , plus, sub, mul-1, div)
    if div > 0:
        dfs(int(num / seq[idx]), idx + 1, plus, sub, mul, div-1)
    


if __name__ == "__main__":
    n = int(input())
    assert 2<=n<=11
    seq = list(map(int, input().split()))
    plus, sub, mul, div = list(map(int, input().split()))
    
    MAX = -10e9
    MIN = 10e9
    
    dfs(seq[0], 1 ,plus, sub, mul, div)
    print(MAX)
    print(MIN)
    

