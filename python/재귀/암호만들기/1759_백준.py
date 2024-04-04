# https://www.acmicpc.net/problem/1759
# 암호만들기

import sys
input = sys.stdin.readline

n = list(map(int, input().split()))
arr = list(input().split())
check = [False] * n[1]
arr.sort()
answer = []

def finder(lst):
    if len(lst) == n[0]:
        lst.sort()
        if lst not in answer:
            answer.append(lst)
        return
    
    for i in range(len(lst), n[1]):
        if check[i] == False and 1 <= (('a' in lst) + ('e' in lst) + ('i' in lst) + ('o' in lst) + ('u' in lst)) <= (n[0]-2):
            check[i] = True
            finder(lst + [arr[i]])
            check[i] = False
finder([])
for lst in answer:
    print(*lst)