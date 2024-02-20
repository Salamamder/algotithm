# 다이나믹 문제 연습
# 1, 2, 3 더하기 3
# 정수 n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 문제 
# (n < 1,000,000)

def DP_1(n):
    arr = [1, 1, 2, 4]
    if n < 4:
        return arr[n]
    
    for i in range(4,n+1):
        arr.append(arr[i-1]+arr[i-2]+arr[i-3])
    answer = arr[i]
    return answer
print(DP_1(10))


n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
    
def DP_1(n):
    arr = [1, 1, 2, 4]
    if n < 4:
        return arr[n]
    
    for i in range(4,n+1):
        arr.append(arr[i-1]+arr[i-2]+arr[i-3])
    answer = arr[n]
    return answer

for i in range(n):
    print(DP_1(a(i))%1000000009)
    
    
    # -------------------------
    
def DP_1(n):
    arr = [1, 1, 2, 4]
    if n < 4:
        return arr[n]
    
    for i in range(4,n+1):
        arr.append(arr[i-1]+arr[i-2]+arr[i-3])
    answer = arr
    return answer

n = int(input())
N = []
for _ in range(n):
    N.append(int(input()))
    # print(DP_1(N)%1000000009)
answer = DP_1(max(N))
for i in range(n):
    print(answer[answer[i]])
    
    # 위에꺼는 메모리 초과가 발생
    # 여러번 만들어져서 그런 듯
    # 한 번만 만들고 불러오는 방식이 좋아보임
    
    
n = int(input())

for _ in range(n):
    m = int(input())
    arr = [0] * (m+1)
    
    for i in range(1, m+1):
        if i == 0:
            arr[i] = 1
        elif i == 2:
            arr[i] =2
        elif i == 3:
            arr[i]=4
        else:
            arr[i] = arr[i-1]+arr[i-2]+arr[i-3]
    
    print(arr[m]%1000000009)
    
    # 이래도 메모리 초과네???
    
import sys
input = sys.stdin.readline

dp = [1,2,4,7]
for i in range(int(input())):
    n = int(input())
    for j in range(len(dp), n):
        dp.append((dp[-3]+dp[-2]+dp[-1])%1000000009)
    print(dp[n-1])
# -------이 방식은 되네 하 참...
# 위에껀 인터넷 참고가 어느정도 된 것

# 내가 만든거 개선하면

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
dp = [1, 1, 2, 4]
for i in range(4, max(arr)):
    dp.append((dp[-1]+dp[-2]+dp[-3])%1000000009)
for i in arr:
    print(dp[i])
# 이것도 메모리 초과가 뜨네;;;

# 한 번 더 개선
n = int(input())
dp = [1,1,2,4]
for i in range(n):
    m = int(input())
    for j in range(len(dp)-1, m):
        dp.append((dp[-1]+dp[-2]+dp[-3])%1000000009)