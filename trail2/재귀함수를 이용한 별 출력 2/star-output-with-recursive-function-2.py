n = int(input())

# Please write your code here.
def print_star(n):
    # 종료 조건: n == 0 일 때 return 하면, n == 1 로 복귀하면서 print를 시작
    if n == 0:
        return

    print("* " * n)
    print_star(n-1)
    print("* " * n)

print_star(n)