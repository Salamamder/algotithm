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

n = int(input)

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
    
    print(arr[m])
