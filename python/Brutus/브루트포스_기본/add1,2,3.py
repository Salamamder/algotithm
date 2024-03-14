# https://www.acmicpc.net/problem/9095
# 
# DP를 통한 문제풀이도 가능하나 브루트포스를 이용해서 문제를 풀어보는 것이 중요해보입니다.
# 해당 문제는 dp로 푸는 방법은 이해를 했으나 
# 부르트포스를 이용할시에 이해도가 떨어짐
import sys
input = sys.stdin.readline

n = int(input())

def finder(s):
    global count
    for i in range(1, 4):
        arr.append(i)
        if sum(arr) == s:
            count += 1
            arr.pop()
            break
        finder(s)
        arr.pop()
    return count

for _ in range(n):
    s = int(input())
    arr = []
    count = 0
    print(finder(s))