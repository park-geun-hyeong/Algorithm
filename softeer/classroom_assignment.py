import sys
import heapq
read = sys.stdin.readline

# nlogn
def solution(n, times):
    #times.sort(key = lambda x: (x[1], x[0]))
    now_end = 0 
    cnt = 0

    while times:
        end, start = heapq.heappop(times)
        if start>=now_end:
            now_end = end
            cnt += 1
        
        if now_end >=1e9:
            break

    return cnt

if __name__ == "__main__":
    n = int(read().rstrip())
    times = []
    for _ in range(n):
        s,e = map(int, read().split())
        heapq.heappush(times, (e,s))
    #[list(map(int, read().split())) for _ in range(n)]

    print(solution(n,times))
