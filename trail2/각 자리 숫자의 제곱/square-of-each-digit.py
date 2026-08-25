N = int(input())

# Please write your code here.

# 함수의 의미는 n의 각 자리 숫자의 제곱을 구하는 함수.
# n이 한 자리 숫자인 경우 n^2을 return 함이 자명.

def recursive(n):
    if n < 10:
        return n**2

    return recursive(n//10) + recursive(n%10)


print(recursive(N))