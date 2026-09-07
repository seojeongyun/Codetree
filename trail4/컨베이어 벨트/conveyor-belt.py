def rotate(up, down, t):
    for _ in range(t):
        tmp = up[-1]
        up = [down[0]]+up[:-1]
        down = down[1:]+[tmp]

    return up, down

n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
# 3 1
# 1 2 3
# 6 5 1

# 1 1 2
# 3 6 5

d_ = d[::-1]
up, down = rotate(u, d_, t)

print(*up)
print(*down[::-1])
