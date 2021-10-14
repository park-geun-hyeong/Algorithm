import sys
input = sys.stdin.readline

a = list(map(str, input()))
a = sorted(a, reverse=True)
print(''.join(a))
