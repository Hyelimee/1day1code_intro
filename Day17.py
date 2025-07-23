'''
Q. 어떤 단어가 사전순으로 가장 앞서는지 맞추는 프로그램 만들기
[조건] 
1. 대소문자를 구분하지 않음
2. 대소문자 구분을 없앴을 대 똑같은 단어는 주어지지 않음

input : 첫째 줄은 단어의 개수
        다음 n줄은 길이가 최대 20인 단어가 주어짐
        마지막 줄은 0이 주어짐
output :각 줄에 각 테스트케이스에서 사전상 가장 앞서있는 단어를 출력한다
'''

import sys

lines = sys.stdin.readlines()  #입력파일의 텍스트 모두 불러오기

#strip으로 \n 제거하기
a = []
for line in lines:
    a.append(line.strip())

#문자열 -> 숫자변환
word = []
for x in a:
    if x.isdigit():
        word.append(int(x))
    else:
        word.append(x)
#print(word)

#정렬하기
i = 0
while i < len(word):
    if isinstance(word[i], int):    #데이터가 숫자일 때
        if word[i] == 0:  #그 숫자가 0이라면 반복문 중지
            break
        
        num = word[i]
        original = word[i+1:i+1+num]            # 원본 단어들 저장
        lower = [w.lower() for w in original]   # 소문자 버전 저장
        #print(original, lower)

        # 소문자 기준으로 정렬한 후, 가장 앞서는 소문자가 무엇인지 찾기
        min_lower = min(lower)

        # 그 소문자가 어느 인덱스였는지 찾아서 원본 단어 출력
        index = lower.index(min_lower)
        print(original[index])
        i += num + 1