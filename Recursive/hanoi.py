def move(N, start, to):
    print(f"Move {N} disk, from {start} to {to}")

def hanoi(N, start, via, to):
    if N == 1:
        move(1, start, to)
    else:
        hanoi(N-1, start, to, via)
        move(N, start, to)
        hanoi(N-1, via, start, to)
        
if __name__ == '__main__':
    n = int(input())
    hanoi(n, 'A', 'B', 'C')
