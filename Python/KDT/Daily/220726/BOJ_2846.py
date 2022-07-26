'''
* 문제 : 수열 N으로 높이 측정, 2개의 수로 이루어진 높이가 증가 => 오르막길
        가장 큰 오르막길 (차이)
* 접근
    * 항상 증가하는 수열이어야함
'''

n = int(input())
case = list(map(int, input().split()))
uphill = 0
result = []

for i in range(n - 1):
    if case[i] < case[i + 1]:
        uphill += case[i + 1] - case[i] 
        result.append(uphill)
    else:  # 앞 값이 크거나 같을 경우 오르막 초기화
        uphill = 0

result.append(uphill)  # 마지막 순서의 처리

print(max(result))        