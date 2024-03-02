# 백준 1309번 문제  https://www.acmicpc.net/problem/1309
# • 가로로두칸,세로로N칸인동물원이있다
# • 가로,세로로붙어있게배치하면안된다
# • 가능한배치의수

# 점화식을 어떻게 잡는지가 중요
# 결국 동물이 붙어있게 배치하면 안됨
# 가로 2 칸을 하나의 단위라 생각하면
# 없는경우, 왼쪽만 있는경우, 오른쪽만 있는 경우 총 3가지의 경우의 수만으로 풀어야 함

# 하나의 경우를 정하면 그 이전에 와야했을 경우를 정해줄 수 있음

# 바텀탑방식으로 가야하는 건가?
# 처음 올 수 있는 경우의 수 3
# 두 번째 올 수 있는 경우의 수 7
# 0-> 3가지
# 1-> 2가지
# 2-> 2가지
# 우리에 사자를 넣는경우 -> 2씩 추가
# 우리에 사자를 넣지 않는 경우 -> 3씩 추가
# 0은 없는 경우 1은 있는 경우 해서 앞전부터 하나씩 늘려나가면 되려나
# 2차원으로 해서


import sys
input = sys.stdin.readline

n = int(input())
def dp(n):
    d = [[0,0],[1,2]]
    if n < 2:
        return d[n][0]+d[n][1]
    for _ in range(n-1):
        d.append([0,0])
    for i in range(2, n+1):
        d[i][0] = d[i-1][0] + d[i-1][1]
        d[i][1] = 2*(d[i-1][0]) + d[i-1][1]
    return d[n][0]+d[n][1]
print(dp(n))
# 이런형태로 짜여지는데
# 메모리 초과가 무엇입니까 ㅎㅎ 
# 아래는 고치려는 시도
import sys
input = sys.stdin.readline
n = int(input())
d = [[0,0],[1,2]]
if n > 1:
    for _ in range(n-1):
        d.append([0,0])
    
    for i in range(2, n+1):
        d[i][0] = (d[i-1][0] + d[i-1][1])
        d[i][1] = (2*(d[i-1][0]) + d[i-1][1])

print([n][0]+d[n][1])

# 메모리가 초과되어 문제가 된다면 변수를 사용해서 문제를 풀 수 있다.
import sys 
input = sys.stdin.readline
n = int(input())
a, b = 1, 2

for i in range(n):
    a, b = (a+b), (2*a+b)
print((a+b)%9901)
# 문제를 리스트에 안넣고 풀면 가능
# 메모리 문제가 생기면 변수로 문제를 푸는 것도 방법인 듯