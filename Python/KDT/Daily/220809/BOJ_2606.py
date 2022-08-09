'''
- 한 컴퓨터가 바이러스 => 네트워크상 연결된 모든 컴퓨터 바이러스
- 1번 컴퓨터 감염 => 바이러스에 노출된 컴퓨터 수

* 1번과 연결되어 있는 무방향 그래프 문제
'''
# 전체 컴퓨터 수
# 1번 부터 차례대로 라벨링, 100 이하
n = int(input())

# 네트워크상에서 직접 연결되어 있는 컴퓨터 쌍
m = int(input())

# 무방향 그래프에 대한 인접 리스트
graphs = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graphs[u].append(v)
    graphs[v].append(u)


target = graphs[1]
result = set()

# 아직 미완성
