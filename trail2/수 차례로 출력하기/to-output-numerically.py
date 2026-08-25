n = int(input())

# Please write your code here.
def recursive_1toN(n):
    # 종료 조건
    if n == 0:
        return

    # 1 to N 이므로 함수 호출이 print문 실행보다 우선
    recursive_1toN(n-1)
    print(n, end =' ')

def recursive_Nto1(n):
    # 종료 조건
    if n == 0:
        return

    # N to 1 이므로 print문 실행이 함수 호출보다 우선
    print(n, end=' ')
    recursive_Nto1(n-1)

recursive_1toN(n)
print()
recursive_Nto1(n)