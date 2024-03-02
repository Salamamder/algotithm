# https://www.acmicpc.net/problem/11055
# Highest increasing fractional sequence 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().strip().split()))


path = [0]*n
path[0]=arr[0]
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            path[i] = max(path[j]+arr[i], path[i])
        else:
            path[i] = max(path[i], arr[i])
print(max(path))