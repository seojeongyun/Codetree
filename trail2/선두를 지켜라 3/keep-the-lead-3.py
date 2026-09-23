N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
'''
A,B 동일 시작, 같은 방향
N,M

매시간마다 그 시점에 가장 앞선 사람들 모아 명예의 전당
    둘 위치 같으면 둘다
    첨 비어있음
    1시간 간격 - 선두 조합 기록
        새로 기록한 조합이 직전에 기록된 조합과 다르면 조합이 1번 바뀐 것
        첫 기록은 1번 바뀐것으로 카운팅
    
명예의 전당에 올라간 사람 조합 몇번바뀜?
'''
honor =[]
ans = 1
a,b = 0,0
pos_a =[]
pos_b =[]

# a,b 위치 기록
for i in range(N):
    for _ in range(t[i]):
        a += v[i]
        pos_a.append(a)
for i in range(M):
    for _ in range(t2[i]):
        b += v2[i]
        pos_b.append(b)

# 명예의 전당 
for a,b in zip(pos_a,pos_b):
    if a==b:
        honor.append('a,b')
    elif a>b:
        honor.append('a')
    else:
        honor.append('b')

# 조합 변경 횟수 카운팅
prev = honor[0]
for i in range(1,len(honor)):
    if prev != honor[i]:
        ans+=1
        prev = honor[i]
    else:
        continue
print(ans)