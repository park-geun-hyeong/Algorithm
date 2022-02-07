# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=804&sw_prbl_sbms_sn=43603

import sys
import string
from collections import deque
read = sys.stdin.readline

def mk_mat(key):

    alpha = set([i.upper() for i in list(string.ascii_lowercase)])
    KEY=[]
    for k in key:
        if k not in KEY:
            KEY.append(k)

    residual = alpha - set(key) - set('J')

    mat_list = KEY + sorted(list(residual))
    mat = []
    row = []
    for k in mat_list:
        row.append(k)
        if len(row) == 5:
            mat.append(row)
            row = []

    return mat

def split_mes(message):

    message = deque(list(message))
    ordinal = []
    part = []

    while message:
        i = message.popleft()

        if len(part) == 0:
            part.append(i)
            continue

        if len(part) == 1:
            if i == part[0]:
                if i == 'X':
                    part.append('Q')
                else:
                    part.append('X')

                message.appendleft(i)
            else:
                part.append(i)

        if len(part) == 2:
            ordinal.append(part)
            part = []

    if len(part) == 1:
        part.append('X')
        ordinal.append(part)

    return ordinal

def transpose(mat):

    n = len(mat)
    tran_mat = [[0]*n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            tran_mat[col][row] = mat[row][col]

    return tran_mat

def first(m, mat):
    f,s = m
    first_idx = 0
    second_idx = 0
    for row in mat:
        if f in row and s in row:
            for idx, i in enumerate(row):
                if i == f:
                    first_idx = idx+1
                    if first_idx == 5:
                        first_idx = 0
                if i == s:
                    second_idx = idx+1
                    if second_idx == 5:
                        second_idx = 0

            return [row[first_idx], row[second_idx]]
    return False

def second(m, mat):
    f,s = m
    first_idx = 0
    second_idx = 0
    for row in mat:
        if f in row and s in row:
            for idx, i in enumerate(row):
                if i == f:
                    first_idx = idx+1
                    if first_idx ==5:
                        first_idx = 0
                if i == s:
                    second_idx = idx+1
                    if second_idx == 5:
                        second_idx = 0

            return [row[first_idx], row[second_idx]]
    return False

def third(m, mat):
    f,s = m
    n= len(mat)
    first_idx=[0,0]
    second_idx=[0,0]
    for row in range(n):
        for col in range(n):
            if mat[row][col] == f:
                first_idx[0] = row
                first_idx[1] = col
            if mat[row][col] == s:
                second_idx[0] = row
                second_idx[1] = col


    return [mat[first_idx[0]][second_idx[1]], mat[second_idx[0]][first_idx[1]]]


def solution(message, key):

    mat = mk_mat(key)
    mes = split_mes(message)

    ans = []
    for m in mes:
        if first(m, mat) == False:
            if second(m, transpose(mat)) == False:
                ans.extend(third(m,mat))

            else:
                ans.extend(second(m,transpose(mat)))

        else:
            ans.extend(first(m,mat))

    return ''.join(ans)

if __name__ == "__main__":
    message = list(map(str, read().rstrip()))
    key = list(map(str, read().rstrip()))
    print(solution(message, key))

