# https://www.acmicpc.net/problem/10971
# 외판원순회
# Traveling Salesman problem (TSP)

import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(n)]
answer = sys.maxsize
chk = [False] * n


def dfs(lst, now):
    global answer
    if len(lst) == n-1:
        if arr[now][0]:
            answer = min(answer, sum(lst) + arr[now][0])
        return
        
    for i in range(n):
        if chk[i] == False and arr[now][i]:
            
            chk[i] = True
            dfs(lst + [arr[now][i]], i)
            chk[i] = False
                
dfs([], 0)
print(answer)