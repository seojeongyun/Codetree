n = int(input())
answer = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    answer.append((n_i, h_i, w_i))

# Please write your code here.
answer.sort(key=lambda x: x[1])

for answ in answer:
    print(*answ)