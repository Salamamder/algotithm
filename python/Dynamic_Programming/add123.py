# 다이나믹 문제
# 1로 만들기
import math
def ott(n):
    arr = [0, 0, 1, 1, 2]
    for i in range(5, n+1):
        one, two, three = math.inf, math.inf, arr[i-1]
        if i % 3 == 0:
            one = arr[i//3]
        if i % 2 == 0:
            two = arr[i//2]
        arr.append(1+min(one, two, three))
    print(arr[n])
    
ott(10)


# n개의 타일링 문제
# 바텀업방식으로 가능 할 듯 (피보나치와 비슷한 방식의 바텀업이 형성된다.)

def tile(n):
    arr = [0, 1, 2, 3]
    if n < 4:
        return arr[n]
    for i in range(4, n+1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n]
print(tile(5))


# n개의 타일링 2 문제