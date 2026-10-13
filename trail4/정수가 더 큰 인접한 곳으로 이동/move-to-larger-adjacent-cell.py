def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

N, i, j = map(int, input().split())
ci, cj = i-1, j-1
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * N for _ in range(N)]
v[ci][cj] = 1
answer = [arr[ci][cj]]


while True:
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci + di, cj + dj
        if in_range(ni, nj) and arr[ci][cj] < arr[ni][nj]:
            answer.append(arr[ni][nj])
            v[ni][nj] = v[ci][cj] + 1
            ci, cj = ni, nj
            break

    else:
        break

print(*answer)
