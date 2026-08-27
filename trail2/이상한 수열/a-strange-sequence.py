N = int(input())

# Please write your code here.
def recursive(N):
    # 종료 조건
    if N == 1:
        return 1
    elif N == 2:
        return 2
    
    return recursive(int(N/3)) + recursive(N-1)

print(recursive(N))