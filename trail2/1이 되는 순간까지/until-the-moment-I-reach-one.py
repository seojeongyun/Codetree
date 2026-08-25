N = int(input())

# Please write your code here.
def recursive(n, cnt):
    if n == 1:
        answer.append(cnt)
        return

    # 짝수면 2로 나눈 몫
    if n % 2 == 0:
        recursive(n // 2, cnt+1)
    
    # 홀수면 3으로 나눈 몫
    else:
        recursive(n // 3, cnt+1)

answer = []
recursive(N, 0)
print(answer[0])