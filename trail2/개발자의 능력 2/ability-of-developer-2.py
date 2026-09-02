import sys
ab = list(map(int, input().split()))

# Please write your code here.
# 6명을 2명씩 3팀으로 배정
# 팀원들의 능력 총합이 가장 큰 팀과 작은 팀의 차이를 최소화할 수 있게 구성할 때의 차를 출력
answer = sys.maxsize
ab_sum = sum(ab)
N = len(ab)
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                if i != j and i != k and i != l and j != k and j != l and k != l:
                    t1_ab = ab[i] + ab[j]
                    t2_ab = ab[k] + ab[l]
                    t3_ab = ab_sum - t1_ab - t2_ab

                    max_ab = max([t1_ab, t2_ab, t3_ab])
                    min_ab = min([t1_ab, t2_ab, t3_ab])
                    # if answer == 0:
                    #     print(i, j, k, l)
                    #     print(t1_ab, t2_ab, t3_ab)
                    answer = min(answer, max_ab - min_ab)

print(answer)