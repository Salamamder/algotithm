# https://www.acmicpc.net/problem/2156
# 포도주시식

# 3잔 연속으로 마시면 안된다는 조건 -> 까다로움
# 상황을 3가지로 줄이고 상황을 기록하는 check리스트를 만들면 되지 않을까함

# 상황 3가지
# 1. xo
# 2. xoo
# 3. oox

# 1. dp[i-2] + arr[i]  check.append(1)
# 2. dp[i-1] + arr[i]  check.append(2)
# 3. dp[i-1]           check.append(0)

# 올 수 있다 1, 2 -> 여기서 max
# 올 수 없다 3    -> 3번 고르면 됨

 