'''
Q. 촌수 계산
- 무방향
'''
import sys

sys.setrecursionlimit(10000)

def dfs(v, cnt):
    visited[v] = True
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i, cnt)

# 전체 사람 수 => 노드 수
n = int(input())

# 촌수를 계산해야하는 두 사람
p1, p2 = map(int, input().split())  # 시작 node : p1

# 부모 자식들 간의 관계의 개수 => 간선 수
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)  # 0촌 존재 X

# 부모 자식간의 관계를 나타내는 두 번호
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(p1, 0)  # 미완료
