# 2011년 m1월 d1일이 월요일이었다면, m2월 d2일은 무슨 요일인지 구해라.

import sys
input = sys.stdin.readline

m1, d1, m2, d2 = map(int, input().strip().split())
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

for month in range(1, m1):
    d1 += num_of_days[month]

for month in range(1, m2):
    # print(month)
    d2 += num_of_days[month]

if d2-d1:
    diff = d2-d1
    print(days[diff % 7])
else:
    diff = d1-d2
    print(days[diff % 7])
