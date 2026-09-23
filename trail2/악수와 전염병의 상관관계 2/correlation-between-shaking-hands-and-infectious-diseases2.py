N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)] # t초, x&y 악수

# Please write your code here.
'''
N 개발자 수, T 악수 기록 / 각 기록= 어떤 두 개발자가 몇초에 악수?

1. P번 개발자 1명만 전염병 감염
2. 감연된 개발자가 전염병 옮길 수 있는 횟수 K
3. K번 다쓰면 옮기지는 x, 감염된 상태는 유지

악수 = 시간 이른 것 부터 하나씩 처리
각 악수는 그 악수가 일어나기 직전 상태를 기준으로 다음 처리
1. 악수 참여한 두 개발자 각각, 그 개발자가 전염 가능한 상태였으면(= 걸려있었으면) 전염횟수 -1
2. 한쪽 걸리고 다른쪽 감염x상태면: 다른쪽은 새로 감염 and K번 할당받음
3. 모두 감염상태 = 양쪽 다 K -=1

모든 악수를 처리한 뒤 최종적으로 누가 전염병에 걸리게 되는지?
'''
# 개발자 (감염 여부, 전염 횟수)
human = [[0,K] for i in range(N+1)]
# 초기 감염자 
human[P] = [1,K]

# 악수: 시간 이른것부터 처리
handshakes.sort(key=lambda x:x[0])


# 악수 수행
for t, h1, h2 in handshakes:
    # 둘 다 감염되어 있으면 K -= 1
    if human[h1][0] and human[h2][0]:
        if human[h1][1] > 0:
            human[h1][1] -= 1
        if human[h2][1] > 0:
            human[h2][1] -= 1
    # 둘 중 한명만 감염되있으면, 감염된 사람만 K-=1
    elif human[h1][0] or human[h2][0]:
        if human[h1][0]: # h1이 감염된 상태면
            if human[h1][1] > 0:#전염 횟수가 유효하면
                human[h1][1] -=1
                human[h2][0] = 1
        else:
            if human[h2][1] > 0:
                human[h2][1] -= 1
                human[h1][0] = 1
    else:
        continue

# 악수 끝나고 전염된 사람 찾기
ans = ''
for i in range(len(human)):
    if i==0:
        continue
    if human[i][0]:
        ans += '1'
    else:
        ans += '0'
print(ans)
