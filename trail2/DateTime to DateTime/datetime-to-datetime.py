import sys
input = sys.stdin.readline

A, B, C = map(int, input().strip().split())

ref = 60*11+11
diff = ((A-11)*24*60 + B*60 + C) - ref

if diff < 0:
    print(-1)

else:
    print(diff)
