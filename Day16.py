'''
Q. 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 
   주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오
   모든 사람은 1부터 100까지 연속된 번호로 표기함

input : 첫째 줄에는 전체 사람의 수 n이 주어짐
        둘째 줄에는 촌수를 계산해야하는 서로 다른 두 사람의 번호가 주어짐
        셋째 줄에는 부모 자식들간의 관계의 개수 m이 주어짐
        넷째 줄부터는 부모자식간의 관계를 나타내는 두 번호 x, y가 각 줄에 나온다
        이때, 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다
output : 입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다
         두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을때는 -1을 출력한다

[필요한개념]
1. BFS : 너비 우선 탐색
        가까운 노드부터 넓게 탐색하는 방식
        큐(queue)사용(FIFO)
        최단 거리 탐색에 유리함
2. DFS : 깊이 우선 탐색
        한 경로를 끝까지 탐색하는 방식
        재귀 또는 스택 사용(LIFO)
        경로 탐색, 특정 조건 만족여부 확인을 위해 사용         
'''

import sys

n = int(sys.stdin.readline())  #전체 사람의 수
a, b = list(map(int, sys.stdin.readline().strip().split(' ')))  #촌수 계산해야하는 사람의 번호
m = int(sys.stdin.readline())  #부모자식관계의 개수

#가족리스트 만들기
family = []
for i in range(m):
    p, c = map(int, sys.stdin.readline().strip().split(' '))
    family.append([p, c])
#print(family)


#인접리스트 만들기
graph = [[] for _ in range(n+1)]

for u, v in family:
    graph[u].append(v)
    graph[v].append(u)
#print(graph)


#BFS 구현하기(a->b까지 얼마나 가는지 계산)
from collections import deque

visit = [False] * (n+1)

def bfs(start, target):
    queue = deque()
    queue.append((start, 0))  #현재 나의 상태 저장
    visit[start] = True  #나는 한번 들렀으니 True로 변경

    while queue:  #queue가 다 비어있지 않는 한 계속 진행
        current, depth = queue.popleft()   #queue에서 값 꺼내기
        if current == target:
            return depth
        for i in graph[current]:    #current와 인접한 사람 확인
            if not visit[i]:        #방문했는지 안했는지 확인
                visit[i] = True 
                queue.append((i, depth+1))   #그 사람으로 주체 변경+촌수 증가

    return -1   #queue가 비어서 돌릴게 없을때

print(bfs(a, b))

