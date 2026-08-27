n = int(input())

# Please write your code here.
# N이 짝수면 2로 나누고, 홀수면 3을 곱하고 1을 더한다
# 이를 N이 1이 되기 전까지 계속 반복
# 몇 번 반복해야하는가?

def recursive(n, cnt):
    if n == 1:
        return cnt

    if n % 2 == 0:
        return recursive(n//2, cnt+1)
    else:
        return recursive(n*3+1, cnt+1)

cnt = 0
print(recursive(n, cnt))