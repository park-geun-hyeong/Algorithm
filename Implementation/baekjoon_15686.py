import sys 
from itertools import combinations
read= sys.stdin.readline

def distance(house_loc,chicken_loc):
    r1,c1 = house_loc
    r2,c2 = chicken_loc
    return abs(r1-r2) + abs(c1-c2)

def city_chicken_dist(all_house_loc, select_chicken_loc):
    
    city_dist=[]
    for h in all_house_loc:
        c_d = []
        for c in select_chicken_loc:
            c_d.append(distance(h, c))
        city_dist.append(min(c_d))
        
    return sum(city_dist)
        
            
def solution(n,m,graph):
    house_loc=[]
    chicken_loc =[]
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                house_loc.append([i,j])
            elif graph[i][j] == 2:
                chicken_loc.append([i,j])
                
    
    MIN = 10e9
    for i in range(m, 0, -1):
        select_chicken_list = list(combinations(chicken_loc, i))
        for chick_loc in select_chicken_list:
            temp = city_chicken_dist(house_loc, chick_loc)
            MIN = min(temp, MIN)
    
    return MIN

if __name__ == "__main__":
    
    n,m = list(map(int, read().split()))
    graph = [list(map(int,read().split())) for _ in range(n)]
    print(solution(n,m,graph))
