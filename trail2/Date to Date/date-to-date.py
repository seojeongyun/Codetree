import sys
input = sys.stdin.readline

m1, d1, m2, d2 = map(int, input().strip().split())
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for month in range(1, m1):
    d1 += num_of_days[month]
    
for month in range(1, m2):
    d2 += num_of_days[month]
    
print(d2-d1+1)


