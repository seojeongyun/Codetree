# 격자: N x M

# 서로 겹치지 않는 두 직사각형을 적절히 잡아, 
    # 격자 판에 평행

# 두 직사각형 안에 적힌 정수 값들의 총 합을 최대로 하는 프로그램 작성

import sys
input = sys.stdin.readline

def get_summation(rect_num, ul, br):
    val = 0
    ul_i, ul_j = ul
    br_i, br_j = br

    for i in range(ul_i, br_i+1):
        for j in range(ul_j, br_j+1):
            if rect_num == 1:
                v[i][j] = 1
            if rect_num == 2:
                if v[i][j]:
                    return -sys.maxsize
            val += arr[i][j]
    
    return val

N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
answer = -sys.maxsize

# 직사각형 1의 좌상단 잡을 2중 포문
for rect1_ul_i in range(N):
    for rect1_ul_j in range(M):

        # 직사각형 1의 우하단 잡을 2중 포문
        for rect1_br_i in range(rect1_ul_i, N):
            for rect1_br_j in range(rect1_ul_j, M):
                rect1_ul = (rect1_ul_i, rect1_ul_j)
                rect1_br = (rect1_br_i, rect1_br_j)
                #
                v = [[0] * M for _ in range(N)]
                #
                rect1_sum_val = get_summation(1, rect1_ul, rect1_br)

                # 직사각형 2의 좌상단 잡을 2중 포문
                for rect2_ul_i in range(N):
                    for rect2_ul_j in range(M):
                        
                        # 직사각형 2의 우상단 잡을 2중 포문
                        for rect2_br_i in range(rect2_ul_i, N):
                            for rect2_br_j in range(rect2_ul_j, M):
                                rect2_ul = (rect2_ul_i, rect2_ul_j)
                                rect2_br = (rect2_br_i, rect2_br_j)
                                #
                                if not v[rect2_ul_i][rect2_ul_j] and not v[rect2_br_i][rect2_br_j]:
                                    rect2_sum_val = get_summation(2, rect2_ul, rect2_br)
                                    answer = max(answer, rect1_sum_val + rect2_sum_val)


print(answer)