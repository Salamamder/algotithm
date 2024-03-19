# https://www.acmicpc.net/problem/15649
# n과 m 문제
# 재귀, 순열, 비트마스크 이 세 가지 중에서 재귀가 중요하다
# 순열, 비트마스크는 재귀로 구현이 가능하기 때문

# 순서와 관련된 문제라 볼 수 있음
# 가능한 모든 경우를 실행한다 => 정답 
# n: 선택된 숫자개수(길이)
# 길이 M짜리 수열


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


# --- =-= -=- =- =- =- =- =---- -----
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ans = []
chk = [False] * (N+1)

def dfs(n, lst):
    # 종료조건(n에 관련) 처리 + 정답처리
    if n==M: # M개의 수열을 완성
        ans.append(lst)
        return # 조건문을 끝낼는 형태
    
    # 하부단계(함수) 호출
    for j in range(1, N+1):
        if chk[j] == False: # 선택하지 않은 하수일 경우
            chk[j] = True
            dfs(n+1, lst+[j])
            chk[j]=False   # 다녀와서는 비활성화 처리를 해줘야 한다.

dfs(0,[])
for lst in ans:
    print(*lst)