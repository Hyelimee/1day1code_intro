'''
Q. N명에게 각각 다섯장의 카드가 주어졌을 때, 세 장의 카드를 골라 합을 구한 후
   1의자리 수가 가장 큰 사람을 찾는 프로그램을 작성하라

input : 첫줄에는 사람의 수를 나타내는 정수 N이 주어진다
        그 다음 N줄에는 1부터 N번까지 각 사람이 가진 카드가 주어진다
        각 줄에는 1부터 10 사이의 정수가 다섯개씩 주어진다
        각 정수 사이에는 한개의 빈칸이 있다
output : 게임에서 이긴 사람의 번호를 첫번째 줄에 출력한다
         이긴사람이 두명 이상일 경우에는 번호가 가장 큰 사람의 번호를 출력한다         
'''

import sys

N = int(sys.stdin.readline())  #게임에 참여하는 사람의 수
card = []

for _ in range(N):
    a = list(map(int, sys.stdin.readline().strip().split(' ')))
    card.append(a)
#print(card)

#세개의 카드를 뽑아서 더해볼까나
from itertools import combinations

result = []

for i in card:
    sums = []
    combi = combinations(i, 3)
    for j in combi:
        b = sum(j)
        sums.append(b)
    result.append(sums)
#print(result)


#1의자리만 구분하기
re = []
for i in result:
    temp = []
    for j in i:
        temp.append(j % 10)
    re.append(temp)
#print(re)

#인덱스 뽑아오기 + 동점일 때 번호 큰 사람이 이기게
import sys

N = int(sys.stdin.readline())  #게임에 참여하는 사람의 수
card = []

for _ in range(N):
    a = list(map(int, sys.stdin.readline().strip().split(' ')))
    card.append(a)
#print(card)

#세개의 카드를 뽑아서 더해볼까나
from itertools import combinations

result = []

for i in card:
    sums = []
    combi = combinations(i, 3)
    for j in combi:
        b = sum(j)
        sums.append(b)
    result.append(sums)
#print(result)


#1의자리만 구분하기
re = []
for i in result:
    temp = []
    for j in i:
        temp.append(j % 10)
    re.append(temp)
#print(re)

#크기 비교하기
max_num = [max(x) for x in re]
#print(max_num)

#인덱스 뽑아오기 + 동점일 때 번호 큰 사람이 이기게
max_value = max(max_num)

# 마지막으로 max_value를 가진 인덱스를 찾기 (동점일 때 번호가 큰 사람)
for i in range(N-1, -1, -1):
    if max_num[i] == max_value:
        print(i + 1)
        break
