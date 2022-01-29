def solution(n,house):
    house.sort()
    return house[(n-1) // 2]


if __name__ == "__main__":
    n=int(input())
    house = list(map(int, input().split()))
    print(solution(n,house))
