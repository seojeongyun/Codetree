# 격자 : L x L
    # (1, 1)부터 시작
    # 빈칸(0), 함정(1), 벽(2)으로 구성
    # 체스판 밖도 벽으로 간주

# 왕실의 기사
    # 자신의 마력으로 상대를 밀쳐낼 수 있다.
    # 초기 위치 (r, c)
    # 방패를 들고 있어 (r, c)를 좌상단으로 하여 h x w 크기의 직사각형 형태를 띄고 있음
    # 체력은 k로 주어짐

# [1] 기사 이동
    # 상하좌우 중 한 칸 이동
    # 이동하려는 위치에 다른 기사가 있다면 그 기사도 연쇄적으로 한 칸씩 밀려남
    # 기사가 이동하려는 방향의 끝에 벽이 있다면 이동 불가
    # 체스판에서 사라진 기사에게 명령을 내리면 아무런 반응이 없다

# [2] 대결 데미지
    # 기사가 다른 기사를 밀치게 되면, 밀려난 기사는 피해를 입는다
        # 기사가 이동한 곳에서 w * h 직사각형 내에 놓여있는 함정의 수만큼 피해를 입음
    # 피해를 받은 만큼 체력이 깎이게 되며, 현재 체력 이상의 데미지를 받으면 체스판에서 사라진다.
    # 명령을 받은 기사는 피해를 입지 않고, 기사들은 모두 밀린 후에 데미지를 입는다. ***********************
    # 밀렸더라도 함정이 없다면 피해를 입지 않는다.

# Q번에 걸쳐 명령이 주어질 때, Q번 이후 생존한 기사들이 받은 데미지의 총합 출력

# -------------------------------------------------
def in_range(i, j):
    return 0 <= i < L and 0 <= j < L
# -------------------------------------------------
def move(kn, d):
    q = []
    pset = set()

    q.append(kn-1)
    pset.add(kn-1)

    while q:
        num = q.pop(0)
        ci, cj, h, w, k = knight[num]
        ni, nj = ci + dis[d], cj + djs[d]

        sset = set()
        for i in range(ni, ni + h):
            for j in range(nj, nj + w):
                sset.add((i, j))
                if not in_range(i, j) or arr[i][j] == 2: # 벽을 만난다면 종료
                    return set()

        # 여기까지 왔다면 벽이 없다는 것이므로, 다른 기사의 영역과 겹치는지 확인
        for idx, (ki, kj, h, w, k) in enumerate(knight):
            if idx != num: # 명령을 받은 기사가 아닌, 다른 기사의 영역 좌표 획득
                kset = set()
                for i in range(ki, ki+h):
                    for j in range(kj, kj+w):
                        kset.add((i, j))

                # 명령을 받은 기사와 다른 기사의 영역이 겹치는지 확인
                for i, j in sset:
                    if (i, j) in kset:
                        q.append(idx)
                        pset.add(idx)

    # 여기까지 왔다면, 미는 동작이 끝난 것, 좌표 갱신
    for idx in pset:
        knight[idx][0] += dis[d]
        knight[idx][1] += djs[d]

    return pset
# -------------------------------------------------
def damage(kn, pset):
    for idx, (ki, kj, h, w, k) in enumerate(knight):
        if idx + 1 == kn: continue # 명령을 받은 기사 i라면 skip
        #
        # 밀려난 기사라면: attacked가 1이라면
        if idx in pset:
            # 밀려난 곳의 w*h 직사각형 내에 놓여있는 함정의 수만큼 피해를 입는다.
            damage = 0
            for i in range(ki, ki+h):
                for j in range(kj, kj+w):
                    if arr[i][j] == 1:
                        damage += 1
            knight[idx][-1] = k - damage
# -------------------------------------------------
# -------------------------------------------------
# -------------------------------------------------
# -------------------------------------------------

# 입력
L, N, Q = map(int, input().split()) # L: 격자 크기 / N: 기사 수 / Q: 명령 수
arr = [list(map(int, input().split())) for _ in range(L)]
knight = []
for _ in range(N):
    r, c, h, w, k = map(int, input().split())
    knight.append([r-1, c-1, h, w, k])
command = [list(map(int, input().split())) for _ in range(Q)]

#
answ_ref = [x[:] for x in knight]
answer = 0

# di, dj: 상 우 하 좌
dis, djs = (-1, 0, 1, 0), (0, 1, 0, -1)

# 명령 실행 시작
removed = set()
for i, d in command:
    if i in removed: continue

    # 기사의 이동
    pset = move(i, d)

    # 데미지 처리
    damage(i, pset)

    # 체력이 음수가 된 기사가 있다면, alive = 0
    for idx, (ki, kj, h, w, k) in enumerate(knight):
        if k <= 0:
            removed.add(idx+1)
            knight[idx] = [0, 0, 0, 0, 0]

# 생존한 기사들이 총 받은 데미지의 합
for idx, (ki, kj, h, w, k) in enumerate(knight):
    if idx+1 not in removed:
        answer += answ_ref[idx][-1] - knight[idx][-1]

print(answer)


