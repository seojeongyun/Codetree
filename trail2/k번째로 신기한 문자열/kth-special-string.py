n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
lst = []
t_len = len(t)
for string in str:
    if list(string)[:t_len] == list(t):
        lst.append(string)

lst.sort()
print(lst[k-1])
