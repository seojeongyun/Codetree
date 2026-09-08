# 2011년 m1월 d1일이 월요일이었다면, m2월 d2일은 무슨 요일인지 구해라.

import sys
input = sys.stdin.readline

m1, d1, m2, d2 = map(int, input().strip().split())
day = input().strip()
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_dict = {
    'Mon' : 0,
    'Tue' : 1,
    'Wed' : 2,
    'Thu' : 3,
    'Fri' : 4,
    'Sat' : 5,
    'Sun' : 6,
}

for month in range(1, m1):
    d1 += num_of_days[month]

for month in range(1, m2):
    d2 += num_of_days[month]

diff = d2-d1
if days_dict[day] <= diff % 7:
    answer = diff//7 + 1
else:
    answer = diff//7
print(answer)
