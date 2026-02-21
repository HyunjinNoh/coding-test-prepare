# 이코테 그리디 p.96
# 3. 숫자 카드 게임

N, M = map(int, input().split())
result = 0 # 최종 결과값 담는 변수 초기화

for i in range(N):
    one_line_list = list(map(int, input().split()))
    min_num_per_line = min(one_line_list)
    result = max(result, min_num_per_line) # 원래 result와 비교

print(result)