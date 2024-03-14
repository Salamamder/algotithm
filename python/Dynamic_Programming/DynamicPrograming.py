# 다이나믹이라는 문제는 점화식과 비슷하다.
# 점화식이라는 것은 뭔가 다이나믹이랑 비슷하다는 느낌을 주는구
# 1, 2, 3 더하기로 문제를 만들자면
import math

def onetwothree(n):
    #먼저 점화식 내용을 만들어준다.
    arr = [1, 1, 2, 4]
    if n < 4:
        return arr[n]
    for i in range(4, n+1):
        arr.append(arr[i-1]+arr[i-2]+arr[i-3])
    return arr[n]

print(onetwothree(10))

# 카드구매하
# 카드 n개를 구매해야 한다.
# i 번째 카팩은 i개의 카드를 담고 있다.가격은 p[i] 원입니다.
# 카드 n개를 구입하는 비용의 최댓값을 구하는 문제이다.
# 점화식개념으로 생각하면 1개 살 때 2 개 살때 생각해서 더해주면 될 듯 함
card_price= [1,5,6,7]
# n장 산다고 할 때
def card(n):
    one, two, three, four = 0, 0, 0, 0
    arr = [0, 1, 5, 6, 10]
    if n < 5:
        return arr[n]
    for i in range(5, n+1):
        arr.append(max(arr[i-1]+card_price[0], arr[i-2]+card_price[1], arr[i-3]+card_price[2], arr[i-4]+card_price[3]))
    return arr[n]
        
        
print(card(8))


# 카드문제 중복 안되게 하는 방법 -> 2차원의 dp의 방식과 유사하다고 

# 우오오오오오오오 만들었다.
# dp 2차원의 형
def dp_2(n):
    arr = [[0]*12 for _ in range(n+1)]
    # 초깃값 설정
    arr[1][2:11] = [1]*9
    # 초깃값 설정 완료
    if n < 2:
        return arr[n]
    # 그 이전 단계에서 해당 값의 전과 윗 값의 합을 넣으면 된다.
    for i in range(2, n+1):
        for j in range(2,11):
            arr[i][j] = arr[i-1][j-1]+ arr[i-1][j+1]
    return arr[n]
m=2
print(dp_2(4)[m+1])


# 이친수
def leecheonsoo(n):
    # 초깃값 설정이 중요하다 it is imnportant that set the initial value
    arr = [[0]*2 for _ in range(n+1)]
    arr[1][0:2] = [0, 1]
    if n < 2:
        return arr[n]
    for i in range(2, n+1):
        arr[i][0] = arr[i-1][0] + arr[i-1][1]
        arr[i][1] = arr[i-1][0]
    return arr[n]
            
print(leecheonsoo(7))

#

