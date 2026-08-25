n = int(input())

# Please write your code here.
def print_star(n):
    # 종료 조건
    if n == 0:
        return

    # i번째 줄에 i개의 별을 출력
    # 재귀 함수가 복귀하면서 별을 출력해야함
    # 즉, 함수 호출이 우선

    print_star(n-1)
    print('*' * n)

print_star(n)