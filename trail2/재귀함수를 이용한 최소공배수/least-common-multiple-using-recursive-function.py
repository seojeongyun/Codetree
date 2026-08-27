N = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
# n개의 수의 최소 공배수를 구하는 재귀함수
n = 0

def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def recursive(LCM, n):
    # 종료 조건
    if n == N:
        return LCM
    
    lcm = LCM * arr[n] / GCD(LCM, arr[n])
    
    return recursive(int(lcm), n+1)

print(recursive(arr[0], n))