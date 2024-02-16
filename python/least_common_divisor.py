# 최소공배 Least Common Multiple(LCM)
# 공통된 배수 중에서 가장 작은 정수
# 최소공배수 l = g * (a / g) * (b / g) 이다.
# ㅁa * b 는 최대공약수 * 최소공배수 와 같기에 
# (A * B) / 최대공약수 = 최소공배수 가 된다.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    

def lcd(a, b):
    return (a * b) / gcd(a,b)

a= lcd(5, 10)
print(a)