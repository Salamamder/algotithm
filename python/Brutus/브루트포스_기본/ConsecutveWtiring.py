# https://www.acmicpc.net/problem/1748
# 수 이어 쓰기
import sys
input = sys.stdin.readline

n = int(input())
answer = 0
n_str = list(str(n))
n_len =len(n_str)
answer = 0
if n_len<2:
    answer = n
    print(answer)
else:
    for i in range(1, n_len):
        answer += ((10**i - 10**(i-1)) * i)
    answer += n_len*((n-10**(n_len-1))+1)
    print(answer)
    

# 정답