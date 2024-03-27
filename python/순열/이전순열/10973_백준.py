# https://www.acmicpc.net/problem/10973
#

import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if arr[i] < arr[i-1]:
        for j in range(n-1 , 0, -1):
            if arr[i-1] > arr[j]:
                arr[i-1], arr[j] = arr[j], arr[i-1]
                arr = arr[:i] + sorted(arr[i:], reverse=True)
                print(*arr)
                sys.exit()
arr = [-1]
print(*arr)