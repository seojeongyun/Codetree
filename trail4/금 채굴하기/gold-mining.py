n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


# 금이 있는 위치만 저장
gold_positions = []

for r in range(n):
    for c in range(n):
        if grid[r][c] == 1:
            gold_positions.append((r, c))

answer = 0

# 중심에서 격자 내 가장 먼 칸까지의 최대 거리는 2 * (n - 1)
for k in range(2 * (n - 1) + 1):
    cost = k ** 2 + (k + 1) ** 2

    # 금을 전부 채굴해도 손해라면 해당 k는 검사할 필요가 없음
    if len(gold_positions) * m < cost:
        continue

    for center_r in range(n):
        for center_c in range(n):
            gold_count = 0

            # 전체 격자가 아니라 금이 있는 위치만 검사
            for gold_r, gold_c in gold_positions:
                distance = (
                    abs(center_r - gold_r)
                    + abs(center_c - gold_c)
                )

                if distance <= k:
                    gold_count += 1

            if gold_count * m >= cost:
                answer = max(answer, gold_count)

print(answer)