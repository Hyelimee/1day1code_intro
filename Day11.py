'''
Q. 동-서 사이트로 다리를 지을 수 있는 경우의 수를 구하시오
   [조건]
   1. 한개의 사이트에는 다리 하나만 지을 수 있음
   2. 서쪽보다 동쪽의 사이트가 더 많음(N <= M)
   3. 최대한 다리를 많이 짓기 위해 서쪽의 사이트 개수만큼 다리를 지으려고 함
   4. N과 M 값은 30보다 작은 수 이다

input : 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
        그 다음 줄부터 각각의 테스트 케이스에 대해 강의 서쪽과 동쪽에 있는 사이트의 개수 N, M이 주어진다
output : 각 테스트 케이스에 대해 주어진 조건 하에 다리를 지을 수 있는 경우의 수를 출력한다

[설계]
1. 테스트 개수를 구한 뒤 테스트 케이스에 대한 각 사이트 개수를 리스트에 저장
2. DP를 구현하여 조합값을 계산한다
    2.1. dp[N][M]로 저장될 수 있도록 표 만들기 (30*30)
    2.2. 조합한 값 구해서 넣기
3. 1에서 받아온 사이트 개수를 DP에서 찾아서 출력하기

[필요한 개념]
조합(combination) : 순서를 고려하지 않고 어떤 항목을 선택하는 방법의 수 <-> 순열(permutation)
- 순서가 중요하지 않는 이유 : 서-동으로 짓든 동-서로 짓든 다리는 하나니까
- 조합으로 경우의 수를 표현하는 경우 M은 오름차순으로 정렬되기 때문에 다리가 겹칠 일이 없음
- n개 중 r개를 고른다고 할때 경우의 수 = n! / r!(n-r)!  -> math.factorial 이용해서 풀 수 있음
- **파스칼의 삼각형 구조**
'''

import sys

T = int(sys.stdin.readline()) #테스트 케이스 개수 구하기
site = []

#각 테스트 케이스에 대한 사이트 개수를 리스트에 저장
for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split(' '))
    site.append([N, M])
#print(site)

#DP를 이용하여 최대 30일 때까지 조합값 계산(Bottom-up 방식)
dp= [[0]*30 for _ in range(30)]  #빈 리스트 생성

#조합계산해서 값 넣어주기(파스칼삼각형이용, 모든 값 미리 계산)
for i in range(30):
    for j in range(i+1):
        if j == 0 or i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

#값 출력
for N, M in site:
    print(dp[M][N])
# N < M 이고, M개에서 N개를 구하는거기 때문에 dp[M][N] 이 맞음



'''
DP가 되려면
1. 중복되는 부분의 문제가 있음
2. 중간 결과를 저장해서 재사용함
3. 점화식으로 문제를 정의함 

*추가 방식(지피티 도움)
1. 팩토리얼 방식(이전 계산을 재사용하지 않음)
import math

def combination_factorial(n, r):
   if r>0:
      return 0
   return math.factorial(n) // (math.factorial(r) * math.factorial(n-r)

print(combination_factorial(5, 2))

2. 점화식(파스칼 삼각형을 사용하긴 하지만 구조적으로 저장해서 사용하지 않음)
def combination_recursive(n, r):
   if r == 0 or r == n:
      return 1
   return combination_recursive(n-1, r-1) + combination_recursive(n-1, r)
-> 위 점화식으로 값을 만들고 리스트화 해서 저장(메모이제이션)하면 Top-down DP가 됨
-> 필요한 값만 계산
'''
