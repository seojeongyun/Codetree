n = int(input())

# Please write your code here.
def print_hw(n):
    if n == 0:
        return
    
    print_hw(n-1)

    print('HelloWorld')

print_hw(n)