'''
[구현/시뮬레이션]
input : 첫째 줄에는 응시자의 수 N과 상을 받는 사람의 수 k가 공백을 사이에 두고 주어짐
        둘째 줄에는 각 학생의 점수 x가 공백을 사이에 두고 주어짐
output : 상을 받는 커트라인을 출력하라
        커트라인이란 상을 받는 사람들 중 점수가 가장 낮은 사람의 점수를 말함
'''

import sys

#응시자수N과 상받는사람k 추출
N, k = list(map(int, sys.stdin.readline().split(' ')))

#학생들 점수 추출
score = list(map(int, sys.stdin.readline().split(' ')))

#점수높은 사람순으로 줄세우기
score.sort(reverse=True)

#커트라인 출력
print(score[k-1])