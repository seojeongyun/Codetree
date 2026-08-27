a, b, c = map(int, input().split())

# Please write your code here.
# 세 수를 곱한 후 각 자리 수의 합을 구하기.

num = a * b * c

def recursive(num):
    # 종료 조건
    if num < 10:
        return num
    
    return recursive(num//10) + (num%10)

print(recursive(num))