n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
'''
1차원 직선 위 1초에 1칸씩. 좌우.
A: N번 움직, 얼마나.어느방향으로 움직 = t, d
B: M번 움직 

A,B 바로 직전에 다른위치에 있다가 그 다음번에 같은 위치에 오게 되는 경우 몇번?

처음 = 같은 지점에서 움직, 횟수에 포함 x

로봇 움직인 종료 이후 = 같은 위치에 머물러 있음
'''
# 1. 로봇 이동 위치 저장
a,b = 0,0
pos_a = []
pos_b = []

for i in range(n):
    for _ in range(t[i]):
        if d[i] == 'L':
            a -= 1
        else:
            a += 1
        pos_a.append(a)

for j in range(m):
    for _ in range(t_b[j]):
        if d_b[j] == 'L':
            b -= 1
        else:
            b += 1
        pos_b.append(b)


# 2. 길이 맞추기
max_len = max(len(pos_a), len(pos_b))
for _ in range(max_len-len(pos_a)):
    pos_a.append(pos_a[-1])
for _ in range(max_len-len(pos_b)):
    pos_b.append(pos_b[-1])

# 3. 직전 다른 위치, 다음번 같은 위치 오게 되는 경우 총 몇 번인지 카운팅
prev_a,prev_b = 0,0
ans = 0
for a,b in zip(pos_a,pos_b):
    if a==b and prev_a != prev_b:
        ans += 1
    prev_a = a
    prev_b = b
print(ans)