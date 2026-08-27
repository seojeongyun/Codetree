n = int(input())
name = []
height = []
weight = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
data = list(zip(name, height, weight))
data.sort(key=lambda x: (x[1], -x[2]))

for answer in data:
    print(*answer)