'''
O(n^2) => time limit

import sys
from collections import deque
read = sys.stdin.readline

def solution(n):
    global graph
    ans = [0]*(n+1) 

    for i in range(1, n+1):
        q = deque()
        q.extend(graph[i])
        check = [0]*(n+1)
        check[i] = 1

        cnt = 0 
        for j in range(len(graph[i])):
            check[graph[i][j][0]] = 1
            cnt += graph[i][j][1]
           
        while q:
            target, dist = q.popleft()
            
            for k in graph[target]:
                if check[k[0]] == 0:
                    cnt += k[1] + dist
                    q.append((k[0], k[1] + dist))                   
                    check[k[0]] = 1
            
        ans[i] = cnt

    for i in range(1,n+1):
        print(ans[i])

if __name__ == "__main__":
    n = int(read().rstrip())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        x,y,t = list(map(int, read().split()))
        graph[x].append((y,t))
        graph[y].append((x,t))

    solution(n)

'''
# Using Sub Tree
# leaf node Sub Tree Num: 1

import sys
read = sys.stdin.readline
sys.setrecursionlimit(int(1e6))


def dfs1(current, parrent):

    '''
        1번 노드의 거리합과 전체 노드에 대한 서브트리 개수 구해주기
        down to top
    '''
    global ans, subTree
    subTree[current] = 1

    for i in range(len(graph[current])):
        child = graph[current][i][0]
        dist = graph[current][i][1] 
        
        if child != parrent:
            dfs1(child, current)
            ans[current] += ans[child] + subTree[child] * dist
            subTree[current] += subTree[child]

    return 



def dfs2(current, parrent):
    global ans, subTree

    '''
        각 노드들의 서브트리 개수와 1번 노드의 거리합을 활용하여 
        전체 노드들에 대한 거리합 구해주기

        top to down
    '''
    for i in range(len(graph[current])):
        child = graph[current][i][0]
        dist = graph[current][i][1] 
        
        if child != parrent:
            ans[child] = ans[current] + dist*(n-2*subTree[child]) 
            dfs2(child, current)
    return 


if __name__ == "__main__":
    n = int(read().rstrip())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        x,y,t = list(map(int, read().split()))
        graph[x].append((y,t))
        graph[y].append((x,t))

    ans = [0]*(n+1)
    subTree = [0]*(n+1)

    dfs1(1,1)
    dfs2(1,1)
    for i in range(1,n+1):
        print(ans[i])


