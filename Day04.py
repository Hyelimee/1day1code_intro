'''
Q. 어떤 반의 학생들의 생일이 주어졌을 때,
    가장 나이가 적은 사람과 많은 사람을 구하는 프로그램을 작성하시오
input : 첫째 줄에 반에 있는 학생의 수 n이 주어짐
        다음 n개의 줄에는 각 학생의 이름과 생일이 "이름 dd mm yyyy"형식으로 주어짐
        주어지는 생일은 올바른 날짜이며, 연 월 일은 0으로 시작하지 않는다
        이름이 같거나, 생일이 같은 사람은 없다
output : 첫째 줄에 가장 나이가 적은 사람의 이름
         둘째 줄에 가장 나이가 많은 사람의 이름을 출력한다
'''

import sys
from datetime import date

n = int(sys.stdin.readline())  #반에 있는 학생 수 추출
birth = []

for _ in range(n): #한줄씩 가져와서 이름, 생년월일 추출
    name, d, m, y = sys.stdin.readline().strip().split(' ')
    ymd = date(int(y), int(m), int(d))
    birth.append([name, ymd])

#나이 어린순서대로 정렬 
birth.sort(key=lambda x:x[1], reverse=True)

print(f"{birth[0][0]}\n{birth[-1][0]}") #f-string 써야 둘째줄에 들여쓰기 안됨