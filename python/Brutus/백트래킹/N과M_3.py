# https://www.acmicpc.net/problem/15651
# 같은 수를 여러번 골라도 된다 -> 중복이 허용된다.

import sys
input = sys.stdin.readline
ans = []
N, M = map(int, input().split())

def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return
    
    for j in range(1, N+1):
        dfs(n+1, lst+[j])
    return ans

ans = dfs(0, [])
for lst in ans:
    print(*lst)