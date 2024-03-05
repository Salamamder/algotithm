# https://www.acmicpc.net/problem/6064
# 카잉달력
# 브루투스 방식에서 건너뛰며 계산한다는 개념 도입

# 규칙을 찾고 최단루트를 몇 번 더 확보하는 것이 핵심인 문제

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().strip().split())))
for i in range(n):
    M, N = arr[n][0], arr[n][1]
    x, y = arr[n][2], arr[n][3]
    a, b = 1, 1
    MN_max = M * N
    count = 0
    while True:
        count +=1
        
        
        if a == x and b == y:
            print(count) 
            break
        elif a == x and b != y:
            count += (M-1)
            b = (b+M)%N
            continue
        
        if a < M:
            a += 1
        else:
            a=1
            
        if b<N:
            b+=1
        else:
            b=1
            
        if count > MN_max:
            print(-1)