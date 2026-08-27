n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
data = list(zip(name, height, weight))
prior_name, prior_height = sorted(data, key=lambda x: x[0]), sorted(data, key=lambda x: -x[1])

print('name')
for answer in prior_name:
    print(*answer)

print()
print('height')
for answer in prior_height:
    print(*answer)