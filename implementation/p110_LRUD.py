N = int(input())
plans = input().split()

r, c = 1, 1 #row의 r, col의 c. x, y로 하면 직교좌표계랑 행렬의 표시형식이 달라서 헷갈릴 수 있음.

direction = ['L', 'R', 'U', 'D']
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(direction)):
        if plan == direction[i]:
            tmp_r = r + dr[i] # 조건에 따라 이동한 좌표를 반영할 지 안할 지 결정해야 하기 때문에 x += 대신 임시 변수 사용
            tmp_c = c + dc[i]
    if tmp_r < 1 or tmp_r > N or tmp_c < 1 or tmp_c > N: 
        continue # 현재 반복에서의 아래 코드 실행 안한 채로 다음 반복으로 건너뛰기
    r = tmp_r
    c = tmp_c

print(r, c)