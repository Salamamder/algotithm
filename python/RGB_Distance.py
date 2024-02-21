# RGB거리

# RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.
# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.
# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

# 문제의 핵심은 2차원의 형태로 푸는 것
# D[i][j] = i번 집을 칠했을 때, 1~i번 칠하는 비용의 최솟값
# j = 0 -> 빨강
# j = 1 -> 초록
# j = 2 -> 파랑
# D[i][j] = i번 집을 j로 칠했을 때 1~i번 집을 칠하는 비용의 최솟값

#읽어와야함
import sys
input = sys.stdin.readline
# 읽어오는거 빠르게 만들어줌
RGB = []
n = int(input())
for i in range(n):
    RGB.append(list(map(int, input().strip().split())))
# 읽어왔으니 이제 각 RGB마다 최솟값 더해나가는 과정이 필요함
for i in range(1, n):
# 인덱스는 0~(n-1)까지다 잊지마라
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0]
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1]
    RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1]) + RGB[i][2]

print(min(RGB[n-1]))

# 여기서 문제가 있던 부분 
# RGB.append(list(map(int, input().strip().split())))    -> 이건 됨
# RGB.append([map(int, input().strip().split())])        -> 이건 안됨 -> 에러 떴음(인지할 걳)