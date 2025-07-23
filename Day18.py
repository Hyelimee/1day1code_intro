'''
Q. 친구관계리스트를 바탕으로 상근이의 결혼식에 초대할 사람의 수를 구하라
   상근이의 동기는 모두 N명이고, 이 학생들의 학번은 모두 1부터 N까지다.
   상근이의 학번은 1이다.

input : 첫째 줄에 상근이의 동기의 수 n이 주어진다
        둘째 줄에는 리스트의 길이 m이 주어진다
        다음 줄부터 m개 줄에는 친구관계 ab가 주어진다(a-b 양방향 친구)
output : 첫째 줄에 상근이의 결혼식에 초대하는 동기의 수를 출력한다
'''
import sys

N = int(sys.stdin.readline())  #전체 동기의 수
M = int(sys.stdin.readline())  #친구관계 리스트의 수

F = [] #친구관계 저장하기
for i in range(M):
    ab = list(map(int, sys.stdin.readline().strip().split(' ')))
    F.append(ab)
#print(F)

#인접리스트 만들기
graph = [[] for _ in range(N+1)]

for a, b in F:
    graph[a].append(b)
    graph[b].append(a)
#print(graph)


#한명씩 거쳐가면서 관련된 사람들 체크하기
#친구(한다리), 친구의 친구(두다리)만 세면 됨
from collections import deque

visit = [False] * (N+1)

queue = deque()
queue.append((1, 0))  #현재 나의 상태 저장
visit[1] = True  #나는 한번 들렀으니 True로 변경

while queue:  #queue가 다 비어있지 않는 한 계속 진행
    current, depth = queue.popleft()   #queue에서 값 꺼내기
    if len(graph[1]) == 0:
        print(0)
        break
    if depth == 2:
        print(sum(visit)-1)
        break
    for j in graph[current]:    
        if not visit[j]:       
            visit[j] = True 
            queue.append((j, depth+1))