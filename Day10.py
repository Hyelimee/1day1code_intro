'''
Q. a층 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야한다
   양의 정수 k와 n에 대해 k층 n호에는 몇명이 살고있는지 출력하라
   아파트는 0층부터 있고 각 층에는 1호부터 있으며, 0층 i호에는 i명이 산다

input : 첫번째 줄에 test case의 수 T가 주어진다.
        각 케이스마다 입력으로 첫번쨰 줄에 정수 k, 두번째 줄에 정수 n이 주어진다.
output : 각각의 test case에 대해서 해당 집에 거주민 수를 출력하라 

[설계]
1. 케이스 수 파악 후 두 줄을 한 쌍으로 가져오기
2. 조건에 맞는 알고리즘을 구한다
    2.1. 0층 : 1호는 1명, 2호는 2명, ...., i호는 i명 살고있음  ((<- 다른 층과 계산방식이 다르므로 따로 작성하여 고정하기))
    2.2. 1층 : 1호는 1명, 2호는 1+2명, 3호는 1+2+3명,...,     
    2.3. 2층 : 1호는 1명, 2호는 1+(1+2)명, 3호는 1+(1+2)+(1+2+3),...,
    *0층 값과 리스트 슬라이싱을 활용하여 값 구하기*
3. 값 출력 print(floor[-1]) #구한 값 중 제일 끝~~ 부분에 있는 값 출력 
'''
import sys

T = int(sys.stdin.readline())  # test case 수 가져오기
a = []

# 1. 두 줄을 한 쌍으로 가져오기(층, 호수)
for _ in range(T):
    k = int(sys.stdin.readline())  # k = 층
    n = int(sys.stdin.readline())  # n = 호
    a.append([k, n])
#print(a)

# 2. 조건에 맞는 알고리즘 구하기
for row in a:
    b, c = row
    floor = [i for i in range(1, c+1)]  # 0층 c호만큼 생성

    if b == 0:  # 0층 
        print(floor[-1])  

    else:       # 0층 외 다른 모든 층 
        for _ in range(b):
            next_floor = []
            for i in range(c):
                next_floor.append(sum(floor[:i+1]))  
            floor = next_floor  # 덮어쓰기로 필요없는 이전 데이터는 지워버림
        print(floor[-1])