'''
Q. 영화감독 숌
- 6이 적어도 3개이상 연속으로 들어가는 수
: 666 -> 1666 -> 2666, ...
'''
# N = 1 => 가장 작은 수, cnt = 1
# N = 2 => 두번째로 작은 수, cnt = 2

N = int(input())
init_val = 666  # 특정 수열 중 제일 작은 수
cnt = 0

while cnt != N:

    if '666' in str(init_val):
        cnt += 1
        ans = init_val

    init_val += 1

print(ans)