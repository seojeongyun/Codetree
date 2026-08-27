n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.

answer = list(zip(name, korean, english, math))
answer.sort(key=lambda x:(-x[1], -x[2], -x[3]))

for answ in answer:
    print(*answ)