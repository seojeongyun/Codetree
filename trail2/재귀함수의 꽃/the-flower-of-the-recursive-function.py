N = int(input())

# Please write your code here.
def recursive(n):
    # 종료 조건
    # n == 0 일 때 return해야, n == 1로 복귀하므로, 이 때부터 출력하면 됨
    if n == 0:
        return

    print(n, end = ' ')
    recursive(n-1)
    print(n, end = ' ')

recursive(N)

