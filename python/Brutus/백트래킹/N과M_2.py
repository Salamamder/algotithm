# https://www.acmicpc.net/problem/15650
# N과 M문제 두 번째
# 오름차순이여야 한다는 조건이 붙었음


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ans = []

def dfs(n, lst, s):
    if n == M:
        ans.append(lst)
        return
    
    for j in range(s, N+1):
        dfs(n+1, lst+[j], j+1)
    return ans

ans = dfs(0, [], 1)
for lst in ans:
    print(*lst)