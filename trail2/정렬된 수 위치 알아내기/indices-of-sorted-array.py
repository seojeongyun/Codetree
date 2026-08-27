n = int(input())
sequence = list(map(int, input().split()))


# Please write your code here.
answer = []
sorted_sequence = sorted(sequence)

for i in range(len(sequence)):
    for j in range(len(sorted_sequence)):
        if sequence[i] == sorted_sequence[j]:
            if j+1 not in answer:
                answer.append(j+1)
                break

print(*answer)