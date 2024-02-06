# 나머지연산
# 10007로 나눈 나머지 -> 정답이 너무 커지는 경우가 존재
# 너무커진다 -> int, long long을 넘어가는 경우
# 정답을 다 구하고 나머지를 구하는 것이 아니고 갱신때마다 나머지를 계산한다.

# (A + B) % M = (A % M) + (B % M) % M
-2 % 3 # 파이썬에 경우 이 결과값이 1 이 나오지만 c, java에서는 -2가 나온다
# 이것을 방지하기 위해 나누는 m을 기준 -m<값<m -> 0 < 값+m < 2m으로 만들고 나머지 계산


#최대공약수 greatest commmon divisor
def greatest_common_divisior(a, b):
    g=1
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            g = i
    return g

a = greatest_common_divisior(5, 10)
print(a)

# 위에 식은 최대공약수 구하는 코드, 시간복잡도(N) = max(a, b)가 된다.

#ㅇ 유클리드 호제법 => 시간복잡도가 log(n)이 된다. 어쨌든 빠르다는 듯
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
b = gcd(5,10)
print(b)
# 16 ,24
# 16/24 = 16*몫 + 16%24
# 몫 = 16%24 + 몫%24