# https://www.acmicpc.net/problem/9095
# 123더하기

import sys
input = sys.stdin.readline

n = int(input())
answer = [0,1,2,3]

def finder(a, answer):
    if len(answer) == n+1 or n<4:
        print(answer[n])
        return
    
    for i in range(a, n):        
        finder(len(answer), lst)


# --------------------------------------------------
import sys

# 이거 되는거 같은데
input = sys.stdin.readline


def finder(lst):
    global cnt
    if sum(lst) > n:
        return
    
    elif sum(lst) == n:
        cnt += 1
        
    for i in range(1,4):
        finder(lst+[i])

r = int(input())
for _ in range(r):
    cnt = 0
    n = int(input())
    finder([])
    print(cnt)

# 재귀 성공