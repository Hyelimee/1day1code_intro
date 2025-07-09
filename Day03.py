'''
아래와 같은 조건에 따라 정렬
1. 길이가 짧은 것 부터
2. 길이가 같으면 사전 순으로
3. 중복된 단어는 하나만 남기기 

input : 첫째줄에 단어의 개수 N이 주어짐
        둘째줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 한 단어가 주어짐
        주어지는 문자열의 길이는 50을 넘지 않음
output : 조건에 따라 정렬하여 단어를 출력함
'''
'''
import sys

N = int(sys.stdin.readline())  #단어 개수 가져오기
arr = []  #길이, 단어 저장할 리스트

#한 줄씩 읽어오기
for _ in range(N):
    word = sys.stdin.readline().strip()
    length = len(word)
    arr.append([length, word])

#알파벳 오름차순
arr.sort(key=lambda x:x[1])

#길이 오름차순 
arr.sort(key=lambda x:x[0])

#중복제거 for문 
result = []

for value in arr:
    if value not in result:
        result.append(value)

#결과 출력 
for i in result:
    print(i[1])

*시간초과 발생함 : 두번의 정렬과 리스트로 인해서?*    
'''

import sys

N = int(sys.stdin.readline())  #단어 개수 가져오기
arr = []  #길이, 단어 저장할 리스트

#한 줄씩 읽어오기
for _ in range(N):
    word = sys.stdin.readline().strip()
    length = len(word)
    arr.append([length, word])  # O(N)

#중복제거
words = list(set(tuple(x) for x in arr))  # O(N)

#알파벳 오름차순
words.sort(key=lambda x:x[1])  # O(NlogN)

#길이 오름차순 
words.sort(key=lambda x:x[0])  # O(NlogN)

#결과 출력 
for word in words:  # O(N)
    print(word[1])

'''
중복 제거를 위해 'value not in result'를 사용하면
value 값이 result에 있는지 없는지 찾기위해 매번 result를 확인해야함
 => 시간 복잡도 O(N)
그런데 여기에 있는 value 값들을 모두 진행해줘야 하므로 
 => 시간 복잡도 O(N)
총 O(N²) 가 된다.

그러나 set을 이용하면 O(N)이므로 훨씬 효율적  
'''