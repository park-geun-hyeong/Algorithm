import sys
import heapq
read =sys.stdin.readline

def solution(card):
    
    heapq.heapify(card)
    sumation= 0
    if len(card) == 1:
        return 0
    elif len(card) == 2:
        return card[0] + card[1]

    while card:
        try:
            first = heapq.heappop(card)
            second = heapq.heappop(card)
            now_sum = first+second
            sumation += now_sum
            heapq.heappush(card, now_sum)
        
        except IndexError:
            break

    return sumation

if __name__ =="__main__":
    n = int(input())
    card = []
    for _ in range(n):
        card.append(int(read().strip()))
        
    print(solution(card))
