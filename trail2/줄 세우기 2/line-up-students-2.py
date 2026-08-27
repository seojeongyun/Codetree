n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.

# 키 오름차순 > 몸무게 내림차순
students.sort(key=lambda x:(x[0], -x[1]))

for answer in students:
    print(*answer)