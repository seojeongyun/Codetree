import sys

n = int(input())
arr = list(map(int, input().split()))
max_val = -sys.maxsize

# Please write your code here.
def recursive(n, max_val):
    # 종료 조건: arr을 전부 순회하면 종료
    if n == 0:
        return max_val

    # 최댓값 찾기
    max_val = max(max_val, arr[n-1])
    return recursive(n-1, max_val)



print(recursive(n, max_val))