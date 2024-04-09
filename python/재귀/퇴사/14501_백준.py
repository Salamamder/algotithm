# https://www.acmicpc.net/problem/14501
# 퇴사

import sys
input = sys.stdin.readline
n = input()
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
answer = 0
# lst에는 날짜를 집어넣고 answer에다가 총 수입을 넣자
def finder(lst):
    if sum(lst) >= n:
        answer = max(answer, sum(lst))
        return
    
    for i in range(n):
        