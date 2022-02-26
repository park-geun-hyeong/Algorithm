# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=631

import sys
read = sys.stdin.readline

def solution(n,m,suggest,cases):

    buyer_pay = [0]*n
    revenue = 0
    case_idx = 0
    for i in range(len(suggest)):
        size = suggest[i][0]
        money = suggest[i][1]
        buyer_idx = suggest[i][2]

        if money > buyer_pay[buyer_idx]:
            revenue = revenue - buyer_pay[buyer_idx] + money
            buyer_pay[buyer_idx] = money

        while(case_idx < m and cases[case_idx][0]<=revenue):
            cases[case_idx].append(size)
            case_idx += 1

    while(case_idx < m):
        cases[case_idx].append(-1)
        case_idx += 1

    cases.sort(key = lambda x: x[1])
    return [i[2] for i in cases]

if __name__ == "__main__":

    n = int(read().rstrip())
    suggest = []
    for i in range(n):
        arr = list(map(int, read().split()))
        for j in range(arr[0]):
            suggest.append([arr[1+j*2], arr[2+j*2], i])

    m = int(read().rstrip())
    Q = list(map(int, read().split()))
    cases = []
    for i in range(m):
        cases.append([Q[i],i])

    suggest.sort()
    cases.sort()


    for i in solution(n,m,suggest,cases):
        print(i, end = ' ')

