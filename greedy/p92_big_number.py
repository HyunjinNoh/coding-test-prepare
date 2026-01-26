# 이코테 그리디 p.92
# 2. 큰 수의 법칙

print("입력 시작")

N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))

sum = 0
max = 0
max_next = 0

max_iter = M // K
next_iter = M % K

num_list.sort(reverse=True) # 내림차순 정렬. 시간복잡도 O(NlogN)
max = num_list[0]
max_next = num_list[1]

if(max == max_next):
    sum = max * M
else:
    sum = (max * K * max_iter) + (max_next * next_iter)

print(sum)