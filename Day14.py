'''
Q. 더게임오브데스 게임 하면서 보성이 술맥이려면 영기가 불러야하는 가장 작은 양의 정수 M은?

[조건]
0(영기) : 게임을 시작하는 사람(임의의 정수 M을 외침, 1을 외침)
1 : 0번의 오른쪽
2 : 1번의 오른쪽
...
0 : N-1번의 오른쪽 사람

input : 첫번째 줄에 게임에 참여하는 사람의 수 N과 보성이의 번호 K가 공백을 두고 주어진다
        두번째 줄부터 N줄에 걸쳐 i번 사람이 지목하는 사람의 번호가 주어진다
        자기자신을 지목하는 경우도 존재할 수 있다
output : 영기가 말해야하는 가장 작은 양의 정수 M을 출력한다
         어떤 방법으로도 보성이가 걸리지 않는다면 -1을 출력한다

최소 길을 찾기 위해 순열을 이용한다
'''

import sys

N, K = sys.stdin.readline().split(' ')
#print(N, K)  #참여하는 사람과 보성이 번호 겟

target = []

for _ in range(int(N)):
    a = int(sys.stdin.readline().strip()) #지목하는 번호
    target.append(a)
#print(target)

current = 0 #영기 번호
M = 0       #지목한 사람한테 이동할때마다 하나씩 증가시킬거야
visit = []  #지목했던 번호 저장하는 공간

while True:
    if current == int(K):   #지목된 현재 번호가 보성이 번호와 같다면
        print(M)            #지목한 횟수를 출력
        break
    if current in visit:    #한번 지목했던 번호를 또 지목하는 경우
        print(-1)           #그럼 보성이를 뽑을 일이 영원히 없기때문에 -1을 뱉음
        break
    visit.append(current)      #현재 번호 저장
    current = target[current]  #다음사람 찍기 위해 업데이트
    M += 1                     #한명 거치면 1증가
