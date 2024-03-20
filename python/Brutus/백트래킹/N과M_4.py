# https://www.acmicpc.net/problem/15652
# N과 M 2번문제에서 > 였던 것이 >= 경우의 문제

import sys
input = sys.stdin.readline
ans = []
N, M = map(int, input().split())

def dfs(n, lst, s):
    if n == M:
        ans.append(lst)
        return
    
    for j in range(s, N+1):
        dfs(n+1, lst+[j], j)

dfs(0, [], 1)
for lst in ans:
    print(*lst)
