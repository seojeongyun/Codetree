n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
answer = 0

for i in range(n):
    for j in range(i, n):
        avg_lst = []
        avg_val = 0
        for k in range(i, j+1):
            avg_lst.append(arr[k])
        avg_val = float(sum(avg_lst)) / len(avg_lst)
        if avg_val in avg_lst:
            # print(avg_val, avg_lst)
            answer += 1

print(answer)