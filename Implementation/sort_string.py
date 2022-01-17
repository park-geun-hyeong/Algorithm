import sys 
read  = sys.stdin.readline

def solution(S):
    string = []
    num =[] 
    for i in S:
        if 48 <= ord(i) <= 57:
            num.append(int(i))
        else: 
            string.append(i)
            
    print(''.join(sorted(string)) + str(sum(num)) )  
if __name__ == "__main__":
    S = list(map(str, read().rstrip()))
    solution(S)
