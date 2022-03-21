import sys
read = sys.stdin.readline

def solution(w,n,price):

    ans = 0
    price.sort(key = lambda x : (-x[1]))

    residual = w
    for i in range(n):
        if residual <= price[i][0]:
            ans += residual * price[i][1]
            break
        residual -= price[i][0]
        ans += price[i][0] * price[i][1]

    return ans


if __name__ == "__main__":
    w,n = map(int, read().split())
    price = [list(map(int, read().split())) for _ in range(n)]

    print(solution(w,n,price))


