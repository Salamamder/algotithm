# https://acmicpc.net/problem/6603
# 로또문제

import sys
input = sys.stdin.readline


def dfs(a, lst):
    if len(lst) == 6:
        answer.append(lst)
        return
    
    for i in range(a, n):
        if arr[i] not in lst:
            dfs(i, lst + [arr[i]])


while True:
    answer = [] # 초기화 필요있어 보임
    arr = list(map(int, input().strip().split()))
    if arr == [0]: # 정지조건
        break
    n = arr[0]
    arr = arr[1:]
    arr.sort()
    
    dfs(0, [])
    for lst in answer:
        print(*lst)
    
    print("")# 빈 줄 하나 출력하래

    # 출력초과가 발생하네
    # 해결 6개만 고르면 되는건데 n개를 골라내서 문제가 발생함

