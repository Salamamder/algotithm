# https://www.acmicpc.net/problem/6064
# 카잉달력
# 브루투스 방식에서 건너뛰며 계산한다는 개념 도입

# 규칙을 찾고 최단루트를 몇 번 더 확보하는 것이 핵심인 문제

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().strip().split())))
for i in range(n):
    M, N = arr[i][0], arr[i][1]
    x, y = arr[i][2], arr[i][3]
    a, b = 1, 1
    MN_max = M * N
    count = 0
    while True:
        count +=1
        if count > MN_max:
            print(-1)
            break
        
        if a == x and b == y:
            print(count) 
            break
        elif a == x and b != y:
            count += (M-1)
            b = (b+M)%N
            continue
        
        if a < M:
            a += 1
        else:
            a=1
            
        if b<N:
            b+=1
        else:
            b=1

# 위에꺼 시간초과 남
            
            import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().strip().split())))
for i in range(n):
    M, N = arr[i][0], arr[i][1]
    x, y = arr[i][2], arr[i][3]
    a, b = 1, 1
    MN_max = M * N
    count = 0
    if m > n:
        while True:
            count +=1
            if count > MN_max:
                print(-1)
                break
            
            if a == x and b == y:
                print(count) 
                break
            elif a == x and b != y:
                count += (M-1)
                b = (b+M)%N
                continue
            
            if a < M:
                a += 1
            else:
                a=1
                
            if b<N:
                b+=1
            else:
                b=1
    else:
        while True:
            count +=1
            if count > MN_max:
                print(-1)
                break
            
            if a == x and b == y:
                print(count) 
                break
            elif a != x and b == y:
                count += (N-1)
                a = (a+N)%M
                continue
            
            if a < M:
                a += 1
            else:
                a=1
                
            if b<N:
                b+=1
            else:
                b=1

# 위의 방식도 시간초과가 발생
# 연산과정을 대량으로 줄일 필요가 있음
# 특이한 식을 발견해야 함
# x가 맞는지 확인하는 방법은 (count-x)%M==0 and (count-y)%N==0 으로하면 됨 
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().strip().split())))
def finder(M,N,x,y):
    a, b = 1, 1
    MN_max = M * N
    count = x
    while count < MN_max:
        if (count-x)%M==0 and (count-y)%N==0:
            return count
        count += M
    return -1
        
for i in range(n):
    M, N = arr[i][0], arr[i][1]
    x, y = arr[i][2], arr[i][3]
    print(finder(M,N,x,y))

# 위의 방법은 맞음 -> 시간적 문제 그리고 "<=" 이거 잘 확인 할 것 