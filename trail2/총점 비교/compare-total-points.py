n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.
answer = list(zip(name, score1, score2, score3))
answer.sort(key=lambda x: x[1]+x[2]+x[3])

for answ in answer:
    print(*answ)