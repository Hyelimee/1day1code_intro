'''
Q. 방향없는 그래프가 주어졌을 때, 연결요소(connected component)의 개수를 구하라

input : 첫째줄에 정점의 개수 N과 간선의 개수 M이 주어진다
        둘째줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다
        같은 간선은 한번만 주어진다
output : 첫째 줄에 연결 요소의 개수를 출력한다

*연결요소 : 간선이 이어져있는 집합을 하나라고 생각
'''

import sys
sys.setrecursionlimit(10**6)

N, M = sys.stdin.readline().split(' ')
#print(N, M)

uv_line = []

for _ in range(int(M)):
    uv_line.append(list(map(int, sys.stdin.readline().strip().split(' '))))

#print(uv_line)


#인접리스트 만들기
graph = [[] for _ in range(int(N)+1)]

for u, v in uv_line:
    graph[u].append(v)
    graph[v].append(u)

#print(graph)

visit = [False] * (int(N)+1)


#어려웠던 부분 : DFS 구현하기
def dfs(node):
    visit[node] = True
    for x in graph[node]:   #정점과 이어진 다른 정점들 파악 후
        if not visit[x]:    #그 정점이 언급된적 있는지 확인하고
            dfs(x)          #안되어있으면 dfs 계속 반복



ans = 0  #연결요소 개수 초기화
for i in range(1, int(N)+1):
    if not visit[i]:   #언급된적이 없으면 다음 아이 확인
        ans += 1
        dfs(i)
print(ans)