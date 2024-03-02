# https://www.acmicpc.net/problem/9465
# 스티커문제
# 문제 내용으로 따지면 동물원 문제와 유형은 비슷

import sys

input = sys.stdin.readline

n = int(input())
# --문제의 수--
for _ in range(n):
    arr = []
    # --단위 블록--
    m = int(input())
    for _ in range(2):
        arr.append(list(map(int, input().strip().split())))

    # --문제알고리즘--
    answer = 0
    arr_2 = []
    for _ in range(2):
        arr_2.append([0]*m)
    if m == 1:
        print(max(arr[0][0], arr[1][0]))

    elif m <= 2:
        answer = max(arr[0][0]+arr[1][1], arr[0][1]+arr[1][0])
        print(answer)
    
    elif m > 2:
        arr_2[0][0] = arr[0][0]
        arr_2[0][1] = arr[0][1]+arr[1][0]
        arr_2[1][0] = arr[1][0]
        arr_2[1][1] = arr[1][1]+arr[0][0]
        for i in range(2, m):
            arr_2[0][i] = arr[0][i] + max(arr_2[1][i-1], arr_2[1][i-2])
            arr_2[1][i] = arr[1][i] + max(arr_2[0][i-1], arr_2[0][i-2])
        print(max(arr_2[0][i], arr_2[1][i]))
        # 이거 함수로 하려면 안됨 리스트 짜야함
        # 맞췄다다다다다다