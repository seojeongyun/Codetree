n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.


for i in range(n):
    if i % 2 == 0:
        new_arr = sorted(arr[:i+1])
        # print(new_arr)
        print(new_arr[len(new_arr)//2], end=' ')


# 0 -> 0
# 2 -> 1
# 4 -> 2
# 6 -> 3
# 8 -> 4
# 1 2 4 5 6 7 9 10 11