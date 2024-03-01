# https://www.acmicpc.net/problem/1932
# 정수 삼각형

import sys
input = sys.stdin.readline

path_score = []
n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))
path_score = tri

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            path_score[i][j] = path_score[i][j] + path_score[i-1][j]
        elif j == i:
            path_score[i][j] = path_score[i][j] + path_score[i-1][j-1]
        else:
            path_score[i][j] = max(path_score[i-1][j]+path_score[i][j], path_score[i-1][j-1]+path_score[i][j])
print(max(path_score[n-1]))

# 문제해결 (완))