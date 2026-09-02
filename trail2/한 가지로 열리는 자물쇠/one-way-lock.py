N = int(input())
a, b, c = map(int, input().split())

# Please write your code here.
# 자물쇠: 1 이상 N 이하의 정수를 각 자리에 넣을 수 있음. 서로 다른 자리에 같은 수도 가능
# 입력한 번호를 기준번호와 같은 자리끼리 비교
    # 한 자리라도 두 수의 차이의 절댓값이 2 이하면 열림.

# N과 기준 번호가 주어졌을 때 자물쇠를 여는 서로 다른 번호의 개수 구하기

answer = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):   
            if abs(i-a) < 3:
                answer += 1
            elif abs(b-j) < 3:
                answer += 1
            elif abs(c-k) < 3:
                answer +=1

print(answer)