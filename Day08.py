'''
Q. 빙고게임
   1~25까지 자연수를 한 칸 당 하나씩 작성
   빙고를 세 줄 만들고 나면 승리
   사회자가 몇번쨰 수를 부른 후 철수가 "빙고"를 외치는지 출력
input : 첫째 줄부터 다섯째 줄까지 차례대로 한 줄에 다섯개씩 빈칸을 사이에 두고 주어짐
        여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 빈칸을 두고 주어짐
output : 첫째 줄에 사회자가 몇번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력

[계획]
1. 철수가 만든 빙고판 가져오기 (cs)
2. 사회자가 부른 숫자 모으기 (host_1)
3. 사회자가 부른 값을 철수의 빙고판에 표현하는 방법 찾기
    3.1 사회자가 부른 값을 철수의 빙고판에서 X로 바꾸기
    3.2 빙고 한 줄을 확인하는 조건식
4. 한줄 표현되면 +1  bingo += 1
    4.1 한번 +1 한 빙고줄을 다시 카운트 하지 않게 중복 방지설정
5. 값이 총 3이 되면 사회자가 부른 숫자 출력 print(i+1)

[후기]
내 코드를 보면서 이게 "정답입니다"는 나오는데 왜이렇게 더러워보일까.. 어떻게 고치지? 라는 생각을 많이했다.
결과를 출력하는 부분이 계속 중복되니까 내 눈이 너무 피로해지는 느낌?
그래서 그냥 조건 밑에 하나만 적는 방식을 하려고 했더니 틀렸다고 나온다.
일단 실습한 코드를 제출한 후에 해설지를 봤는데 눈에 띄는 문장이 있었다.
((예를 들어 이 문제에서 빙고가 3개일때 정답을 외치는 것이 아니라, 빙고가 3개 이상일 때 정답을 외치는 것 처럼 말이죠))
굳이 꼭 빙고가 세 개 일때만 결과가 출력되게 하려다보니 하나를 불렀을때 빙고가 여러개가 한번에 나올 수 있다는 점을 간과한 것
==를 >=로만 고쳤더니 훨씬 코드 길이가 줄어들고 정답도 맞았다.
'''

import sys

cs = []  #철수의 빙고판 저장할 빈 리스트

#철수 빙고판 가져오기
for i in range(5):
    cs.append(list(map(int, sys.stdin.readline().strip().split())))
    
host = []  #사회자가 부른 숫자를 저장할 빈 리스트

#사회자 숫자 가져오기
for i in range(5):
    host.append(list(map(int, sys.stdin.readline().strip().split())))

#사회자가 부른 값은 굳이 이중리스트일 필요 없다고 생각..
host_1 = [x for row in host for x in row]
#print(host_1)

bingo = 0  #빙고 초기화
bingo_line = set()  #중복검사방지용

for i in range(len(host_1)):
    for row in range(5):
        for j in range(5):
            if cs[row][j] == host_1[i]:
                cs[row][j] = 'X'  #빙고판 X표기 시스템 만들기

                #가로빙고검사
                if cs[row] == ['X'] * 5 and ('row', row) not in bingo_line:
                    bingo += 1
                    bingo_line.add(('row', row))
                    if bingo == 3:
                        print(i+1)  #결과 출력
                        sys.exit()
                #세로빙고검사
                if cs[0][j] == "X" and cs[1][j] == "X" and cs[2][j] == "X" and cs[3][j] == "X" and cs[4][j] == "X" and ('col', j) not in bingo_line:
                    bingo += 1
                    bingo_line.add(('col', j))
                    if bingo == 3:
                        print(i+1)  #결과 출력
                        sys.exit()
                #대각선빙고검사1
                if cs[0][0] == "X" and cs[1][1] == "X" and cs[2][2] == "X" and cs[3][3] == "X" and cs[4][4] == "X" and ('left') not in bingo_line:
                    bingo += 1
                    bingo_line.add('left')
                    if bingo == 3:
                        print(i+1)  #결과 출력
                        sys.exit()
                #대각선빙고검사2
                if cs[0][4] == "X" and cs[1][3] == "X" and cs[2][2] == "X" and cs[3][1] == "X" and cs[4][0] == "X" and ('right') not in bingo_line:
                    bingo += 1
                    bingo_line.add('right')
                    if bingo == 3:
                        print(i+1)  #결과 출력
                        sys.exit()
               
#print(bingo_line)

'''
#수정 코드
import sys

cs = []  #철수의 빙고판 저장할 빈 리스트

#철수 빙고판 가져오기
for i in range(5):
    cs.append(list(map(int, sys.stdin.readline().strip().split())))
    
host = []  #사회자가 부른 숫자를 저장할 빈 리스트

#사회자 숫자 가져오기
for i in range(5):
    host.append(list(map(int, sys.stdin.readline().strip().split())))

#사회자가 부른 값은 굳이 이중리스트일 필요 없다고 생각..
host_1 = [x for row in host for x in row]
#print(host_1)

bingo = 0  #빙고 초기화
bingo_line = set()  #중복검사방지용

for i in range(len(host_1)):
    for row in range(5):
        for j in range(5):
            if cs[row][j] == host_1[i]:
                cs[row][j] = 'X'  #빙고판 X표기 시스템 만들기

                #가로빙고검사
                if cs[row] == ['X'] * 5 and ('row', row) not in bingo_line:
                    bingo += 1
                    bingo_line.add(('row', row))
                #세로빙고검사
                if cs[0][j] == "X" and cs[1][j] == "X" and cs[2][j] == "X" and cs[3][j] == "X" and cs[4][j] == "X" and ('col', j) not in bingo_line:
                    bingo += 1
                    bingo_line.add(('col', j))
                #대각선빙고검사1
                if cs[0][0] == "X" and cs[1][1] == "X" and cs[2][2] == "X" and cs[3][3] == "X" and cs[4][4] == "X" and ('left') not in bingo_line:
                    bingo += 1
                    bingo_line.add('left')
                #대각선빙고검사2
                if cs[0][4] == "X" and cs[1][3] == "X" and cs[2][2] == "X" and cs[3][1] == "X" and cs[4][0] == "X" and ('right') not in bingo_line:
                    bingo += 1
                    bingo_line.add('right')
                
                #빙고 세 줄 됐는지 확인
                if bingo >= 3:
                    print(i+1)  #결과 출력
                    sys.exit()  #나가기
#print(bingo_line)
'''

        
    

