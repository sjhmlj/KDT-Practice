'''
* 로그가 주어질 때 현재 회사에 있는 모든 사람 출력
enter : 들어옴
leave : 나감
==> enter가 있으나 leave가 없는 인원이 대상
* 동명이인 X, 대소문자 구분 O
'''

n = int(input())
log = {}

for i in range(n):
    name, status = input().split()
    log[name] = status

in_company = []
for name in log:
    if log[name] == 'enter':
        in_company.append(name)

result = sorted(in_company, reverse=True)

for worker in result:
    print(worker)