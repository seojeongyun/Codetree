import sys

abilities = list(map(int, input().split()))

# Please write your code here.
answer = sys.maxsize
sum_abilities = sum(abilities)

for i in range(len(abilities)):
    for j in range(i+1, len(abilities)):
        for k in range(j+1, len(abilities)):
            answer = min(answer, abs((sum_abilities - (abilities[i] + abilities[j] + abilities[k]) - (abilities[i] + abilities[j] + abilities[k]))))

print(answer)