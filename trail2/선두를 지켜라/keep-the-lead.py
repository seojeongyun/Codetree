n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi) # 속도
    t.append(ti) # 시간

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
'''
A,B 동일 시작점, 같은 방향
A N/ B M
특정 속도, 특정 시간만큼 이동

선두 몇 번 바뀌는지 찾아 출력
공동 선두 = 바뀌지 않았다고 판단
'''
a,b = 0,0
pos_a = []
pos_b = []
for ai in range(n):
    for _ in range(t[ai]):
        a += v[ai]
        pos_a.append(a)

for bi in range(m):
   for _ in range(t2[bi]):
        b += v2[bi]
        pos_b.append(b)


ans = 0
faster = None
for a, b in zip(pos_a,pos_b):
    if a>b:
        c ='a'
    elif b>a:
        c='b'
    else:
        continue
        
    if not faster:
        faster = c
    if faster != c:
        ans+=1
        faster = c
print(ans)
