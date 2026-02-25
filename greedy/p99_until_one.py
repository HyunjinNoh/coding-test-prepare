# 이코테 그리디 p.99
# 4. 1이 될 때까지

''' 초기 코드
N, K = map(int, input().split())
result = N
count = 0
while True:
    if result == 1:
        break
    elif result % K == 0:
        result = result // K
        count += 1
    else:
        result = result - 1
        count += 1
print(count)
'''

N, K = map(int, input().split())
count = 0

while True:
    if N < K: #더 이상 나눌 수 없을 때를 뜻함. 반복된 나눗셈을 해야할 땐 나머지 변수를 두는 거 보다 이런 방식 생각해보기
        break

    else:
        # STEP 1: 가까운 K의 배수를 먼저 만들고, 뺄셈 횟수를 먼저 한꺼번에 더함
        now_near_multiple = (N // K) * K # while 반복문 안에서 계속 가까운 k의 배수를 갱신해야 하는 이유: N // K 결과가 항상 K의 배수라고 보장할 수 없다.
        count += N - now_near_multiple  # 가까운 k의 배수를 만들기 위해 n에서 1을 빼야 할 횟수! 뺄셈 횟수를 count에 먼저 더해놓기
        N = now_near_multiple

        # STEP 2: 가까운 K의 배수인 N에서 K를 나눠 N과 count 갱신
        N //= K
        count += 1

count += N - 1 # N이 K보다는 작지만 아직 1은 아닐 때, 1까지 빼야 하는 횟수 더함
print(count)
