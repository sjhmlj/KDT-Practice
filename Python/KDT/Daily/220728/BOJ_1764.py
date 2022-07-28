'''
* 듣도 못한 경우, 보도 못한 경우 => 듣도 보도 못한 명단
'''
# set 활용
n, m = map(int, input().split())
no_heared = set()
no_seen = set()

for i in range(n):
    h = input()
    no_heared.add(h)

for i in range(m):
    s = input()
    no_seen.add(s)

no_know = sorted(no_heared & no_seen)

print(len(no_know))
for i in no_know:
    print(i)


# list and dict 풀이 (100 % 까지 갔다가 실패)
# n, m = map(int, input().split())
# no_heared = []
# no_seen = []
# temp = {}
# for i in range(n):
#     no_heared = input()
#     temp[no_heared]

# for j in range(m):
#     no_seen.append(input())


# cnt = max(temp.values())

# result = sorted(filter(lambda x : temp[x] == cnt, temp), key = lambda x : x)

# print(len(result))
# for i in result:
#     print(i)


