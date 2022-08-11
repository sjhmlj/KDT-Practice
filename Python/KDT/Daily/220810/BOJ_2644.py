import sys

sys.stdin = open('input_2644.txt')

# 전체 사람 수
n = int(input())
# 촌수를 알고싶은 두 사람
p1, p2 = map(int, input().split())
# 관계 수
m = int(input())
# DFS를 위한 그래프 및 방문 리스트 초기화
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
# 무방향 그래프 초기화
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

stack = []
stack.append((p1, 0))
visited[p1] = True
result = []
result = -1
# [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]
while stack:
    adjs, cnt = stack.pop()

    if adjs == p2:
        result = cnt
        break
    for adj in graph[adjs]:
        if not visited[adj]:
            visited[adj] = True
            stack.append((adj, cnt + 1))

print(result)