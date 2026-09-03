from itertools import combinations
N, M = map(int, input().split())

# Please write your code here.
'''
입
출
    조합의 개수 만큰 줄에 걸쳐 한 줄에 하나씩
    사전순으로 앞선 조합부터 추력,
    한조합 내에는 정수들 오름차순 정렬하여 출력
문
    1이상 N이하 정수
    M 개 선태
    만들수 있는 모든 조합
'''

comb = set(list(combinations(range(1,N+1),M)))
for com in comb:
    for i in range(M):
        print(com[i], end=' ')
    print()
