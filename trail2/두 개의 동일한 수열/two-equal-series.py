n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
if (set(A) | set(B)) == set(A) or (set(A) | set(B)) == set(B):
    print('Yes')

else:
    print('No')