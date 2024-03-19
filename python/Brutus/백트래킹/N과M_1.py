# https://www.acmicpc.net/problem/15649
# n과 m 문제
# 재귀, 순열, 비트마스크 이 세 가지 중에서 재귀가 중요하다
# 순열, 비트마스크는 재귀로 구현이 가능하기 때문

# 순서와 관련된 문제라 볼 수 있음
# 


n = [3, 1]

chk = [false]*n[0]

def finder(cnt, N, M):
    global cnt
    if cnt == M:
        answer.append(chk)
        return 
    for i in range(N):
        cnt += 1
        chk[i] = True
        finder(i,N-cnt)
        chk[i]=False
    answer.pop()


# -------------------------
def finder(cnt, N, M):
    for i in range(4):
        cnt +=1
        chk[i]=True
        if cnt == M:
            aws.append(chk)
            break
        finder[cnt,N,M]
        chk[i] = False
        
# ------------------------
n = [3, 1]

chk = [false]*n[0]

def finder(cnt, N, M):
    global cnt
    if cnt == M:
        print(*answer)
        return 
    for i in range(N):
        if not chk[i]:
            cnt += 1
            chk[i] = True
            answer.append(i+1)
            finder(cnt,N,M)
            chk[i]=False
    answer.pop()