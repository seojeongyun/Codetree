N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.
# 1부터 N까지.
# 모든 자리에 대해 첫 번째 조합과 거리가 2 이내이거나, 두 번째 조합과 거리가 2이내면 열림

'''
    예시: N = 9
    첫 번째 조합: 1,2,3
    두 번째 조합: 4,5,6

    1,9,5 일 때 첫 번째 조합과 조건을 만족
    -> 원형으로 된 자물쇠임을 고려.
    -> 두 수를 비교할 때, min((큰 수 - 작은수), (9-큰 수 + 작은 수))
'''

answer = 0 

for i in range(1, N+1):
    a1_max, a1_min = max(a1, i), min(a1, i)
    a2_max, a2_min = max(a2, i), min(a2, i)
    for j in range(1, N+1):
        b1_max, b1_min = max(b1, j), min(b1, j)
        b2_max, b2_min = max(b2, j), min(b2, j)
        for k in range(1, N+1):
            c1_max, c1_min = max(c1, k), min(c1, k)
            c2_max, c2_min = max(c2, k), min(c2, k)
            
            # 첫 번째 조합과의 거리 비교
            a1_dist = min(a1_max - a1_min, N - a1_max + a1_min)
            b1_dist = min(b1_max - b1_min, N - b1_max + b1_min)
            c1_dist = min(c1_max - c1_min, N - c1_max + c1_min)

            # 두 번째 조합과의 거리 비교
            a2_dist = min(a2_max - a2_min, N - a2_max + a2_min)
            b2_dist = min(b2_max - b2_min, N - b2_max + b2_min)
            c2_dist = min(c2_max - c2_min, N - c2_max + c2_min)

            if 0 <= a1_dist < 3 and 0 <= b1_dist < 3 and 0 <= c1_dist < 3:
                answer += 1

            elif 0 <= a2_dist < 3 and 0 <= b2_dist < 3 and 0 <= c2_dist < 3:
                answer += 1

            # 예제 1번의 경우 i,j,k == 3,4,5 에서 중복 카운팅 됨

print(answer)