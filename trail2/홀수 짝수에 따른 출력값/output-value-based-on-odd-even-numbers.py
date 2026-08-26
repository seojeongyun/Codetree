N = int(input())

# Please write your code here.
def recursive(n):
    if n == 1:
        return 1 
    elif n == 2:
        return 2

    return n + recursive(n-2)

print(recursive(N))


