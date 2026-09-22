N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
'''
학생 N, 1~N번호
한 학생이 K번 이상 벌칙 받으면 벌금

M번에 걸쳐 벌칙에 걸린 학생의 번호 순서대로 주어짐
최초로 벌금을 내게되는 학생?
'''
ans = -1
pay = [0]*(1+N)
for m in student:
    if K == 1:
        ans = m
        break
    pay[m] += 1
    if pay[m] >= K:
        ans = m
        break
print(ans)
