# 두 수 X, Y가 주어지면, X 이상 Y 이하 수 중 각 자리 숫자 합이 최대인 값을 출력

import sys
input = sys.stdin.readline
answer = -sys.maxsize

X, Y = map(int, input().strip().split())

for i in range(X, Y+1):
    lst = list(str(i))
    val = 0
    for j in range(len(lst)):
        val += int(lst[j])

    answer = max(answer, val)

print(answer)