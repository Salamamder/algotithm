# https://www.acmicpc.net/problem/2156
# 포도주시식

# 3잔 연속으로 마시면 안된다는 조건 -> 까다로움
# 상황을 3가지로 줄이고 상황을 기록하는 check리스트를 만들면 되지 않을까함

# 상황 3가지
# 1. xo
# 2. xoo
# 3. x 
# 위의 3가지 상황은 모든상황에 대응할 수 있음 즉 if문 사용 없이 max값 쳐서 사용하면 됨
# check리스트 같은거 따로 만들 필요도 없어짐 

# 1. dp[i-2] + arr[i]  check.append(1)
# 2. dp[i-1] + arr[i]  check.append(2)
# 3. dp[i-1]           check.append(0)

# 올 수 있다 1, 2 -> 여기서 max
# 올 수 없다 3    -> 3번 고르면 됨

# 읽어오고 변수 선언 영역
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
path = [0]*n
path[0] = arr[0]

#알고리즘영역
if n>1:
    path[1] = arr[0]+arr[1]
if n>2:
    path[2] = max(arr[0]+arr[1], arr[1]+arr[2])
for i in range(3, n):
    path[i] = max(path[i-2]+arr[i], path[i-3] + arr[i-1] + arr[i], path[i-1])
print(path[n-1])

# 왜 틀린거지? 
# 원인 발견: path 2 는 oox xoo 둘중 하나라고 생각했는데 oxo의 경우가 존재함

import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
path = [0]*n
path[0] = arr[0]

#알고리즘영역
if n>1:
    path[1] = arr[0]+arr[1]
if n>2:
    path[2] = max(path[1],arr[1]+arr[2],arr[0]+arr[2])
for i in range(3, n):
    path[i] = max(path[i-2]+arr[i], path[i-3] + arr[i-1] + arr[i], path[i-1])
print(path[n-1])

# 드디어 맞았다....