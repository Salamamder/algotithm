# https://www.acmicpc.net/problem/1476
# 날짜 계산 문제
# 브루투스 이용

import sys
input = sys.stdin.readline
E, S, M = list(map(int, input().strip().split()))

# 일부만 찾아서 해결하는 것이 중요
# 가장 간격이 큰 놈이 S가 28로 가장 크니 요놈을 기준으로 하면 될 듯 함
cnt = 0 # 0으로 시작하지만 1로 봐야함 즉 real cnt == cnt+1
while True:
    if (cnt%15+1)==E and (cnt%28+1)==S and (cnt%19+1)==M:
        break
    if (cnt%28+1==S):
        cnt += 28
        continue
    cnt += 1

print(cnt+1)