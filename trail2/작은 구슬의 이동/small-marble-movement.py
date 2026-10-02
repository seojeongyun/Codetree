'''
NxN 격자 안 1개 구슬
상하좌우 중 특정 방향 1초에 1칸

가장 왼쪽위 (1행,1열), 가장 오른쪽 아래 (N행,N열)
초기: 구슬 = 1행 2열, 왼쪽으로 향하는 구슬

구슬 벽에 부딪히면 움직이는 방향 반대로, 동일 속도로 움직이는 것 반복
방향 바꾸는데 1초 시간 소요 -> 1초 동안 위치변화 x

벽이 아니라면 바라보는 방향으로 1칸 이동

처음 위치, 초기 방향 주어질 때 
T초가 지난 이후 구슬 위치?
'''

# 입력
N, T = map(int, input().split())
R, C, D = input().split() # 구슬 초기 위치(r,c), 방향(d)
R, C = int(R)-1, int(C)-1
direc = {'U':0 ,'D':3 ,'R':1 ,'L':2}
D = direc[D]

dys, dxs = [-1,0,0,1],[0,1,-1,0]

def in_range(x,y):
    return 0<=x<N and 0<=y<N

# T초 동안
for t in range(T):
    nr, nc = R+dys[D], C+dxs[D]
    # 위치가 벽이면: 방향변화
    if not in_range(nr,nc):
        # 방향 변화: D 
        D = abs(3-D) # 2-1 = 1
    # 아니면 위치이동
    else:
        R,C = nr, nc
print(R+1, C+1)