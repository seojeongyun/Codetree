N = int(input())

# Please write your code here.
# 수열: 2, 4, (앞의 두 수의 곱을 100으로 나눈 나머지) ...
# N번째 값을 구하시오.

def recursive(N):
    # 종료 조건
    if N == 1:
        return 2
    elif N == 2:
        return 4

    return (recursive(N-1) * recursive(N-2)) % 100
print(recursive(N))