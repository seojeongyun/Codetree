import sys
input = sys.stdin.readline

A, B, C, D = map(int, input().strip().split())

diff = (C * 60 + D) - (A * 60 + B)
print(diff)