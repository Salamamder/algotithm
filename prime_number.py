# 소수 prime number
# 소수는 2보다 크거나 같 n-1보다 작거나 같은 수로 나누어 떨어지면 안된다.

def prime_number(n):
    if n<2:
        return False
    for i in range(2, n-1):
        if n%i == 0:
            return False
    return True

print(prime_number(10))
print(prime_number(13))
# 이렇게 짜면 시간복잡도 n이 된다.

# 간단한 수학적 개념을 도입하면
# 소수 n인지 확인 하는 방법중에 
# n이 소수가 되려, 2보다 크거 같고 n/2보다 작거나 같은 자연수로 나누어 떨어지면 안된다.
# n = a * b로 표현할 수 있는데 a가 작을수록 b가 커진다 (반비례관계)
# a의 가능한 가장 작은 수는 2이며 이 때 b의 값은 n / 2가 된다. 즉 현실적으로 
# 소수인지 아닌지 판별할 가장 큰 수는 n/2까지만 알아보면 된다.

def pn(n):
    if n < 2:
        return False
    for i in range(2, int(n/2)+1):
        if n%i == 0:
            return False
    return True

print(pn(10))
print(pn(13))


# 또다른 개념으로는 n = a * b로 나타낼 수 있고
# a 가 b보다 크다고 할 경우
# 제곱근n = 제곱근a * 제곱근b 인데 여기서 제곱근 a는 제곱근n보다 크다고 해야 한다. b는 제곱근n 보다 작아야 하고
# 해당개념 이용시 시간복잡도는 제곱근n이된다. 엄청 작아지게 된다.
# 수학자들 이 미친새기들 진짜 엄청나네...

def prn(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

print(prn(10))
print(prn(13))


# n이하의 소수 구하기
# 루트n 이용하고 n이하의 수 모두 계산하면 시간복잡도 n*(n**(1/2))짜리가 나온다.

# 더 빠르게 계산하는 방법으로 
# 에라토스테네스의 체 라는 방법이 있다. 

def eratos(n):
    a = [False, False] + [True]*(n-1)
    primes = []
    
    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
            for i in range(i*2, n+1, i):
                a[i] = False
    return primes

print(eratos(100))
print(eratos(200))
# 여기도 살짝 추가