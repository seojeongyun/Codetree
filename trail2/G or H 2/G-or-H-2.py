n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
# 사진에 찍힌 사람들의 팻말이 G로만 구성 or H로만 구성 or G 개수 == H 개수.
# 가능한 사진의 최대 크기를 구하시오.

MAX_SIZE = max(pos)+1

answer = 0
arr = [0] * MAX_SIZE

for pos, alpha in people:
    arr[int(pos)] = alpha  
# print(arr)

# 사진의 window 크기
for window in range(MAX_SIZE): # 
    # 사진의 시작 지점
    for i in range(MAX_SIZE-window):
        lst = []
        idx = []
        G_cnt, H_cnt = 0, 0
        for j in range(i, i+window+1):
            # print(i, i+window)
            if arr[i+window] == 0:
                break

            if arr[j] != 0:
                lst.append(arr[j])
                idx.append(j)
        if len(lst) > 0:
            # G나 H로만 이루어진 경우
            if len(set(lst)) == 1:
                # print(lst)
                answer = max(answer, idx[-1]-idx[0])
            # G와 H의 개수가 같은 경우
            else:
                for char in lst:
                    if char == 'G':
                        G_cnt += 1
                    else:
                        H_cnt += 1
                
                if G_cnt == H_cnt:
                    # print(lst)
                    answer = max(answer, idx[-1]-idx[0])

if answer == 1:
    print(0)
else:
    print(answer)