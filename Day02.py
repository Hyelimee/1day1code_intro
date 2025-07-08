'''
input : 첫째줄에 온라인 저지 회원의 수 N이 주어진다
        둘째줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다
        나이는 1보다 크거나 같으며 200보다 작거나 같은 정수
        이름은 알파벳 대소문자로 이루어져있고 길이가 100보다 작거나 같은 문자열
        입력은 가입한 순서로 주어짐
output : 첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로
         한줄에 한명씩 나이와 이름을 공백으로 구분해 출력한다.
'''

import sys

N = int(sys.stdin.readline())  #온라인 저지 회원 수 읽기
member = []
age_min = 1

#회원정보저장
for _ in range(N):
    l = sys.stdin.readline().strip().split(' ')
    l[0] = int(l[0])    #나이를 int로 변환
    member.append(l)    

#회원 정렬
sort_mem = sorted(member, key=lambda x:x[0])    
#print(sort_mem)

#output
for i in sort_mem:
    print(*i)
