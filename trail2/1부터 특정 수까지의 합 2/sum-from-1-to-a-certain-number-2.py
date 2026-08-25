N = int(input())

# Please write your code here.

# 함수의 의미는, 1부터 n까지 더하는 함수.
# 따라서, recursive(1) = 1 임이 자명함.

def recursive(n):
    # 종료 조건: recursive(1) = 1 임을 활용
    if n == 1:
        return 1

    return recursive(n-1) + n

print(recursive(N))