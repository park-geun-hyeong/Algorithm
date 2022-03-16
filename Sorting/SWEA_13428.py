'''
T = int(input())

for test_case in range(1,T+1):

    num = list(input())
    length = len(num)
    if length == 1:
        num = int(num[0])
        print(f"#{test_case} {num} {num}")
        continue

    MAX= MIN = int(''.join(num))
    for i in range(length-1):
        for j in range(i, length):
            num[i],num[j] = num[j],num[i]
            if int(''.join(num))>MAX:
                MAX = int(''.join(num))
            if num[0] != '0' and int(''.join(num))<MIN:
                MIN = int(''.join(num))
            num[i], num[j] = num[j], num[i]

    print(f"#{test_case} {MIN} {MAX}")
'''

T = int(input())

def find_min(num:list):
    for idx, i in enumerate(num):
        if (idx == 0 and i == '1'):
            continue
        elif i == min(num[idx:]):
            continue
        else:
            new = [(IDX, int(i)) for IDX, i in enumerate(num[idx+1:])]
            new.sort(key=lambda x: (x[1], -x[0]))
            if idx == 0:
                if new[0][1] != 0:
                    min_idx = 1 + new[0][0]
                    num[idx], num[min_idx] = num[min_idx], num[idx]
                    return int(''.join(num))
                else:
                    for x,y in new:
                        if y == 0:
                            continue
                        elif y >= int(i):
                            break
                        else:
                            min_idx = 1 + x
                            num[idx], num[min_idx] = num[min_idx], num[idx]
                            return int(''.join(num))
            else:
                min_idx = idx + 1 + new[0][0]
                num[idx], num[min_idx] = num[min_idx], num[idx]
                return int(''.join(num))

    return int(''.join(num))

def find_max(num:list):

    for idx, i in enumerate(num):
        if i == max(num[idx:]):
            continue
        else:
            new = [(IDX, int(i)) for IDX, i in enumerate(num[idx+1:])]
            new.sort(key=lambda x: (-x[1], -x[0]))
            max_idx = idx + 1 + new[0][0]
            num[idx], num[max_idx] = num[max_idx], num[idx]
            return int(''.join(num))

    return int(''.join(num))

for test_case in range(1,T+1):

    num = list(input())
    num2 = num.copy()
    length = len(num)
    if length == 1:
        num = int(num[0])
        print(f"#{test_case} {num} {num}")
        continue

    MIN = find_min(num)
    MAX = find_max(num2)
    print(f"#{test_case} {MIN} {MAX}")













