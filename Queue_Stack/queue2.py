from collections import deque


def solution(n):
    q = deque()
    for i in range(1, n + 1):
        q.append(i)

    while (len(q) > 1):
        q.popleft()
        q.append(q.popleft())

    return q[0]


if __name__ == "__main__":
    n = int(input())
    print(solution(n))

