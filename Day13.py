'''
Q. N개의 정수로 이루어진 순열이 주어졌을때, 순열 사이클의 개수를 구하라
input : 첫째줄에 테스트 케이스의 개수 T가 주어짐
        각 테스트 케이스의 첫째 줄에는 순열의 크기 N이 주어짐
        각 테스트 케이스의 둘째 줄에는 순열이 주어짐
        각 정수는 공백으로 구분되어 있음
output : 각 테스트 케이스마다 입력으로 주어진 순열에 존재하는 순열 사이클의 개수 출력

[필요한 개념]
- 순열 : 1부터 N까지 수를 한번씩 모두 사용해서 만든 배열
 > 나타내는 방식(예 N=8)
   위치 : 1 2 3 4 5 6 7 8
     값 : 3 2 7 8 1 4 5 6
 > 위치 1에 있는 값이 3 이므로 1->3 이라고 표현
   그런식으로 이어보면 1->3->7->5->1 이 되면서 다시 1로 돌아옴 = 순열사이클

[설계]
1. 테스트케이스 가져와서 리스트로 정리하기
2. 순열조합 탐색하기
'''

import sys

T = int(sys.stdin.readline()) # 테스트 케이스 가져오기

testcase = []

for _ in range(T):
    N = int(sys.stdin.readline())
    P = [0] + list(map(int, sys.stdin.readline().strip().split(' ')))
    testcase.append([N, P])
#print(testcase)

#순열사이클탐색
for i in testcase:
    N = i[0]
    P = i[1]
    visit = [0] * (N+1)  #탐색 유무 확인용
    cycle = 0

    for j in range(1, N+1):
        if visit[j] == 0:    #시작점이 사이클에 사용됐었는지 확인
             current = j
             while visit[current] == 0:   #순열사이클 찾기용
                 visit[current] = 1
                 current = P[current]
             cycle += 1
    
    print(cycle)
                 
