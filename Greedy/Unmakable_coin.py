
'''
 First code: Poor code in terms of time complexity and space complexity
#######################################################################

from itertools import combinations

def solution(coin):
    
    dp = [0]*(sum(coin) + 1)
    if min(coin) > 1:
        print(1)
        return
    else: 
        for num in range(1, n + 1):
            if num == 1:
                for i in coin:
                    dp[i] = 1
            
            elif num == n:
                dp[sum(coin)] = 1
                
            else:
                combi = list(combinations(coin, num))
                for j in combi:
                    dp[sum(j)] = 1
    
    for i in range(1, sum(coin) + 1):
        if dp[i] == 0:
            print(i)
            return
        
if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    solution(coin)

'''

n= int(input())
coin = list(map(int, input().split()))
coin.sort()

target = 1
for i in coin:
    if target<i:
        break
    
    target += i
    
print(target)
