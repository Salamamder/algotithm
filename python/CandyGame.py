# https://www.acmicpc.net/problem/3085
# 사탕게임
# n * n 크기의 테이블에 사탕이 있다
# 인접한 두 칸을 고르고 사탕을 교환한다.
# 그 다음 같은 색으로 이루어진 가장 긴 연속 부분 행 또는 열을 고르는 문제

# 솔직히 문제자체를 이해 못하겠음 -> 

# 브루투스 방식으로 문제 해결을 원할시

# 자리교환은 오른쪽 아래랑만 한다고 해도 전체적으로 보면 교환이 진행이 됨 
# 1. 처음에 터지는게 존재한지 확인 
# 2. 자리를 바꾼 후 터지는지 확인 -> 돌려놓기도 진행
# 3. 1과 2에서 터지는 크기가 최대로 큰게 생길 때마다 갱신하기

# 아놔 이 캔디크러쉬소다문제;;;

# 읽어오는 영역
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input()) for _ in range(n)]

# 전체적으로 터지는게 있는지 확인하는 코드를 def로 만들어놓자
# 스왑때리는 함수 필요하자나
def swapping(n, arr):
    answer = 1
    imsi = 0
    for i in range(n-1):
        for j in range(n-1):
            #바꾸고 확인하고 돌려야함
            # 바꾸기(아래버전)
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            #체크하기
            imsi = check(n, arr)
            if answer < imsi:
                answer = imsi
            # 돌리기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            
            # 바꾸기(우측버전)
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            #체크하기
            imsi = check(n, arr)
            if answer < imsi:
                answer = imsi
            # 돌리기
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
    return answer

# 체크하는 함수
def check(n, arr):
    answer = 1
    for i in range(n):
        for j in range(n):
            count=1
            # 아래로 확인
            while True:
                if i!=n-1 and arr[i][j] == arr[i+1][j]:
                    count += 1
                    i += 1
                elif i==n-1 or arr[i][j] != arr[i+1][j]:
                    if answer < count:
                        answer = count
                    break
            # 우측으로 확인b
            while True:
                if j!=n-1 and arr[i][j] == arr[i][j+1]:
                    count += 1
                    j += 1
                elif  j==n-1 or arr[i][j] != arr[i][j+1]:
                    if answer < count:
                        answer = count
                    break
    return answer
print(swapping(n, arr))

# 틀렸네;;;
# 문제원인 확인해야함 ㅠ

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input()) for _ in range(n)]

# 전체적으로 터지는게 있는지 확인하는 코드를 def로 만들어놓자
# 스왑때리는 함수 필요하자나
def checkandswapping(n, arr):
    answer = check(n, arr)
    imsi = 0
    for i in range(n-1):
        for j in range(n-1):
            #바꾸고 확인하고 돌려야함
            # 바꾸기(아래버전)
            if i+1 < n and arr[i][j] != arr[i+1][j]:
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
                #체크하기
                imsi = check(n, arr)
                answer = max(answer ,imsi)
                # 돌리기
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
                
            # 바꾸기(우측버전)
            if j+1 < n and arr[i][j] != arr[i][j+1]:
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
                #체크하기
                imsi = check(n, arr)
                answer = max(answer ,imsi)
                # 돌리기
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
    return answer

# 체크하는 함수
def check(n, arr):
    answer = 1
    for i in range(n):
        for j in range(n):
            count=1
            # 아래로 확인
            while True:
                if i!=n-1 and arr[i][j] == arr[i+1][j]:
                    count += 1
                    i += 1
                elif i==n-1 or arr[i][j] != arr[i+1][j]:
                    if answer < count:
                        answer = count
                    break
            # 우측으로 확인b
            while True:
                if j!=n-1 and arr[i][j] == arr[i][j+1]:
                    count += 1
                    j += 1
                elif  j==n-1 or arr[i][j] != arr[i][j+1]:
                    if answer < count:
                        answer = count
                    break
    return answer
print(checkandswapping(n, arr))