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
        
    for i in range(1, n):# 여기서 1부터 시작하는 이유는  시작점은 0을 받아서 시작하도록 했고 for i in range에서 i는 도착위치였음 그러니 도착은 0을 제외한 곳에서 나와야 해서
        if chk[i] == False and arr[now][i]:
            
            chk[i] = True
            dfs(lst + [arr[now][i]], i)
            chk[i] = False
                
dfs([], 0)
print(answer)