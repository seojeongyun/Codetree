n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
'''
NxM 이차원 영역의 각 위치에 자연수
2가지 종류의 블럭 중 1개를 격자 내에 배치

칸 안에 적힌 수의 합 최대가 될 때 결과를 출력

블럭 자유롭게 회전 & 뒤집을 수 O
'''
def rotate(block):
    rotated = [(x,-y) for y,x in block]
    return rotated

def normalization(block):
    min_y = min(y for y,x in block)
    min_x = min(x for y,x in block)
    return tuple(sorted((y-min_y, x-min_x) for y,x in block))

# 블럭정의 & 회전 좌표 생성
blocks = [[(0,0),(1,0),(1,1)], [(0,0),(0,1),(0,2)]]
rotated_blocks = set()

for block in blocks:
    rotated_block = block
    for _ in range(4):
        rotated_blocks.add(normalization(rotated_block))
        rotated_block = rotate(rotated_block)

max_sum = 0
# NxM영역에서
for i in range(n):
    for j in range(m):
        # 블럭 영역 순회(이동)
        for block in rotated_blocks:
            if all(0<=i+y<n and 0<=j+x<m for y,x in block):
                block_sum = sum(grid[y+i][x+j] for y,x in block)
                max_sum = max(max_sum, block_sum)
print(max_sum)


