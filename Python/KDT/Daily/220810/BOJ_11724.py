'''
Q. 연결요소의 개수
- 무방향 그래프 => 연결 요소의 개수
'''
import sys

sys.setrecursionlimit(10000)  # 최대 재귀함수 제한 해제

# dfs 
def dfs(graph, v, visited):
    visited[v] = True  # visited 초기값 
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# input : N, M
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # 그래프 초기화 (idx : 0 사용 x)

visited = [False] * (N + 1)  # 각 정점 탐색 여부 판별 리스트
count = 0

# 무방향 그래프
for _ in range(M):
    # 노드 양 끝 점 u, v
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    if not visited[i]:
        count += 1
        dfs(graph, i, visited)
        
print(count)

