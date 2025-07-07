'''
input : 아홉 줄에 걸쳐 난쟁이들의 키가 주어진다.
        주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르다
        가능한 정답이 여러가지인 경우에는 아무거나 출력한다.
output : 일곱 난쟁이의 키를 오름차순으로 출력한다.
         일곱 난쟁이를 찾을 수 없는 경우는 없다.
'''
import sys
import random

l = []

for _ in range(9):
    a = int(sys.stdin.readline())
    l.append(a)

while True: 
    rand = random.sample(l, 7)
    if sum(rand) == 100:
        rand.sort()
        for i in rand:
            print(i)
        break