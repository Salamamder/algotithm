# https://www.acmicpc.net/problem/2309
# 일곱난쟁이 문제
# 입력으로 9 난쟁이의 키가 주어지고 7명의 키의 합이 100을 만족하는 난쟁이 키를 출력해주면 된다.
import sys
input=sys.stdin.readline

arr = []
for _ in range(9):
    arr.append(int(input()))
arr.sort(reverse=False)
hap = sum(arr)
for i in range(8):
    for j in range(i+1,9):
        if hap-arr[i]-arr[j] == 100:
            arr.pop(j)
            arr.pop(i)
            for m in range(7):
                print(arr[m])
# 문제발생 -> 리스트인덱스관련 문제인 것으로 보임
                
# 아래껀 해결한 버전
import sys
input=sys.stdin.readline

arr = []
for _ in range(9):
    arr.append(int(input()))
a = 0
b = 0
arr.sort(reverse=False)
hap = sum(arr)
for i in range(8):
    for j in range(i+1,9):
        if hap - arr[i] - arr[j] == 100:
            a = i
            b = j
arr.pop(b)
arr.pop(a)
for m in range(7):
    print(arr[m])

# 원인 : 반복문중에 조건이 부합하면 리스트 원소를 삭제했는데 삭제된 원소로 인해 리스트의 크기가 줄고 이로인해 리스트 인덱스 범위 초과라는 상황 발생
# 해결 : 리스트 원소 제거를 반복문이 다 돈 뒤에 행해지도록 함