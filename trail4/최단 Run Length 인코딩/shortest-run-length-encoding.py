# 길이가 N인 문자열 A
# 이 문자열을 오른쪽으로 순환 shift한 뒤 RLE를 적용해 길이가 최소가 되도록
    # K번 순환 shift
    # K == 0이면 그대로

# RLE
    # 연속해서 나온 문자와 연속해서 나온 개수로 나타내는 방식
    # 예를 들어 aaabbbbcaa면 a3b4c1a2가 되며 길이는 8이됨

# 순환 shift를 진행해 나올 수 있는 RLE 이후의 결과중 최소 길이

import sys
from collections import deque
input = sys.stdin.readline

def rotate(A):
    value = A.pop()
    A.appendleft(value)
    
    return A

def RLE(A_str):
    lst = []
    cnt = 1
    for i in range(len(A_str)-1):
        if A_str[i] == A_str[i+1]:
            cnt += 1
        else:
            lst.append(A_str[i])
            lst.append(str(cnt))
            cnt = 1

    return deque(list(''.join(lst)))

A = deque(list(input().strip()))
answer = sys.maxsize

for _ in range(len(A)+1):
    A = rotate(A)
    RLE_A = RLE(A+deque(['eos']))
    answer = min(answer, len(RLE_A))

print(answer)

