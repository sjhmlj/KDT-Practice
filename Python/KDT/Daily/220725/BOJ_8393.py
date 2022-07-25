'''
* 문제 : 1부터 n까지 합
* 접근
    * for loop
'''

n = int(input())
ans = 0

for i in range(1, n + 1):
    ans += i

print(ans)