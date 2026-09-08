import sys
input = sys.stdin.readline

dec = input().strip()
dec_lst = list(map(int, dec))
dec_lst = dec_lst[::-1]
answer = 0

for i, bit in enumerate(dec_lst):
    # print(i, bit, 2**(i)*bit)
    answer += (2 ** i*bit)

print(answer)