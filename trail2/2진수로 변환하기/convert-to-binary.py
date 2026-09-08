import sys
input = sys.stdin.readline

N = int(input().strip())

# [1] 함수 이용
print(bin(N)[2:])

# [2] 나눗셈 이용
# bin_lst = []
# if N == 0:
#     print(0)
# while N > 0:
#     bin_lst.append(N % 2)
#     N = N // 2

# for bit in bin_lst[::-1]:
#     print(bit, end='')
    