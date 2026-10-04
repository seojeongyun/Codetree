'''
1 이상 100 이하 숫자 NxN

열 기준 처리
    1. 행으로 봤을 때 연속으로 M개 이상 같은 숫자가 적힌 폭탄은 터짐
    2. 중력에 의해 폭탄들 drop
    3. M개 이상 연속한 폭탄은 전부 터짐
        3-1. M개 이상 폭탄 쌍 여러개: 동시에 터짐
        터진 이후에 같은 열에 M개이상 같은 숫자 있으면 없어질때까지 터뜨리는 거 반복
[동작]
K번 반복
    [1] 조건에 맞는 폭탄 터뜨리기
    [2] 아래로 떨어뜨리기   
    [3] 터진 과정 반복 후 상자 시계방향으로 90도 돌리기
    [4] 아래로 떨어뜨리기  
K번 회전 진행 후에도 터질 폭탄 남아있으면, 다 터뜨리고 최종 상자 구하기

[출력]
최종적으로 남은 폭탄 수
'''
def debug_print(arr):
    for row in arr:
        print(*row)

# 입력
N,M,K = tuple(map(int,input().split()))
arr =[list(map(int,input().split())) for _ in range(N)]

def rotate(): # 시계, 90도
    arr[:] = [list(row) for row in zip(*(arr[::-1]))]

def drop():
    tmp = [[0]*N for _ in range(N)]
    
    # 열 단위 수행
    for j in range(N):
        next_row = N-1
        for i in range(N-1,-1,-1):
            # 0이 아닌 값 tmp에 저장
            if arr[i][j]:
                tmp[next_row][j] = arr[i][j]
                next_row -= 1
    
    arr[:] = tmp

def bomb():
    # 열 단위 수행    
    for j in range(N):
        prev = -1
        same_cnt = 0
        bomb_coord = []
        
        # 행 단위 수행
        for i in range(N-1,-1,-1):
            
            # 0이면 continue
            if not arr[i][j]:
                if same_cnt >= M:
                    for r in bomb_coord:
                        arr[r][j] = 0
                prev = -1
                same_cnt=0
                bomb_coord = []
                continue
            
            # prev 없으면
            if prev == -1:
                prev = arr[i][j]
                same_cnt = 1
                bomb_coord=[i]

            # 현재 값과 이전값이 같으면
            # 개수 카운팅, 좌표 저장
            elif prev == arr[i][j]: 
                same_cnt += 1
                bomb_coord.append(i)
            else:
                # 값이 달라지면 prev 갱신
                prev = arr[i][j]
                # same_cnt가 M이상인지 확인
                # 이상이면 폭탄 터뜨리기 = 해당 좌표값 0으로 만들기
                if same_cnt >= M:
                    for r in bomb_coord:
                        arr[r][j] = 0
               
                same_cnt = 1
                bomb_coord = [i]
        if same_cnt >= M:
            for r in bomb_coord:
                arr[r][j] = 0

def bomb_until_stable():
    while True:
        # 종료조건: 이전 arr과 bomb을 수행한 후 배열 동일
        before = [row[:] for row in arr]
        bomb()
        if before==arr:
            break
        drop()
        
for _ in range(K):
    bomb_until_stable()
    drop()
    rotate()
    drop()


bomb_until_stable()


cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            cnt+=1
print(cnt)


