def move(n, start, end):
    print(f"Move {n} disk, from {start} to {end}")

def hanoi(n, start ,via ,end):
    if n == 1:
        move(n, start, end)
    else:
        hanoi(n-1, start, end, via)
        move(n, start, end)
        hanoi(n-1, start, via ,end)
        
if __name__ == '__main__':
    n = int(input())
    hanoi(n, 'A', 'B', 'C')
