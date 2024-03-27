# https://www.acmicpc.net/problem/10819
# 차이를 최대로

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
answer = [0]
chk = [False] * n
def dfs(lst):
    imsi = 0
    if len(lst) == n:
        for j in range(1,n):
            imsi += abs(lst[j-1] - lst[j])
        if answer[-1] < imsi:
            answer.append(imsi)
        return
    
    for i in range(n):
        if chk[i] == False:
            chk[i] = True
            dfs(lst + [arr[i]])
            chk[i] = False
            
dfs([])
print(answer[-1])