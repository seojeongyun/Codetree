n, m = map(int, input().split())

d = []
t = []

for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []

for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))


a, b = 0, 0

pos_a = []
pos_b = []

# A의 매초 위치
for i in range(n):
    for _ in range(t[i]):
        if d[i] == 'R':
            a += 1
        else:
            a -= 1
        pos_a.append(a)


# B의 매초 위치
for j in range(m):
    for _ in range(t2[j]):
        if d2[j] == 'R':
            b += 1
        else:
            b -= 1
        pos_b.append(b)


ans = -1
for t, (a, b) in enumerate(zip(pos_a, pos_b)):
    if a == b:
        ans = t + 1
        break

print(ans)