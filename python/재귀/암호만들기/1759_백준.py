# https://www.acmicpc.net/problem/1759
# 암호만들기

import sys
input = sys.stdin.readline

n = list(map(int, input().split()))
arr = list(input().split())
arr.sort()
answer = []

def finder(a, b, lst):
    if len(lst) == n[0]:
        if 0 < ('a' in lst) + ('e' in lst) + ('i' in lst) + ('o' in lst) + ('u' in lst) <= (n[0]-2):
            print("".join(lst))
        return
    
    for i in range(a, n[1]-n[0]+1+b):
        finder(i+1, b+1, lst + [arr[i]])
        
finder(0, 0, [])