'''
enter -> 이모티콘 사용
* enter이후에 중복된 아이디가 있는가 없는가
'''

import sys

input = sys.stdin.readline

n = int(input())
log = set()
cnt = 0

for i in range(n):
    id = input().rstrip()

    if id == 'ENTER':
        log.clear()

    elif id not in log:
        log.add(id)
        cnt += 1

print(cnt)