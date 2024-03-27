# https://www.acmicpc.net/problem/10974

import sys
input = sys.stdin.readline

n = int(input())

def finder(lst):
    if len(lst) == n:
        print(*lst)
        return
    for i in range(1, n+1):
        if i not in lst:
            finder(lst+[i])
finder([])    
    