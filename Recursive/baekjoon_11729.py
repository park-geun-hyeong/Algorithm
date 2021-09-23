def move(n, start, end):
    print(f"{start} {end}")

def hanoi(n, start ,end ,via): 
    if n == 1:
        move(1, start, end)
    else:
        hanoi(n-1, start, via, end)
        move(n, start, end)
        hanoi(n-1, via, end ,start)

c=0
def cnt(n, start, end, via):    
    global c
    
    if n==1:
        c += 1
    else:
        cnt(n-1, start,via,end)
        c += 1
        cnt(n-1, start, end ,via)
              
    return c
                
if __name__ == '__main__':
    n = int(input())
    print(cnt(n, '1', '3','2'))
    hanoi(n, '1', '3', '2')
