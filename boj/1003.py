# 피보나치 함수
# https://www.acmicpc.net/problem/1003

"""
recursion(4) = recursion(3) + recursion(2)
-> recursion(4) = recursion(1) + recursion(0) + recursion(1) + recursion(1) + recursion(0) == 2 3
recursion(3) = recursion(2) + recursion(1)
-> recursion(3) = recursion(1) + recursion(0) + recursion(1) == 1 2
recursion(2) = recursion(1) + recursion(0)
recursion(1) = 1
recursion(0) = 0

0 - 1 0
1 - 0 1
2 - 1 1
3 - 1 2
4 - 2 3
5 - 3 5
6 - 5 8
결국 이거도 피보나치처럼 간다? 그러면 메모이제이션이나 재귀로 해결 가능해보임 -> 근데 문제의 최대 입력값은 40 (3억 회로 에러)
arr[i] = [arr[i - 2][0] + arr[i - 1][0], arr[i - 2][1] + arr[i - 1][1]]
"""

def memoization(n):
  arr = [[0, 0]] * (n + 1)
  arr[0] = [1, 0]

  if n == 0: return arr[0]
  arr[1] = [0, 1]

  for i in range(2, len(arr)):
    arr[i] = [arr[i - 2][0] + arr[i - 1][0], arr[i - 2][1] + arr[i - 1][1]]

  return arr[n]

"""
0 - 1 0
1 - 0 1
2 - 1 1
3 - 1 2
4 - 2 3
5 - 3 5
6 - 5 8
i - (i - 1)[1], (i - 1)[0] + (i - 1)[1]
"""
def recursion_memoization(n):
  global arr2

  if arr2[n][0] != -1: return arr2[n]

  index = recursion_memoization(n - 1)

  arr2[n][0] = index[1]
  arr2[n][1] = index[0] + index[1]

  return arr2[n]
 

T = int(input())
MAX = 40
# arr2 = [[-1, -1]] * (MAX + 1) 틀린 방식이었네
arr2 = [[-1, -1] for _ in range(MAX + 1)]
arr2[0] = [1, 0]
arr2[1] = [0, 1]

for _ in range(T):
  N = int(input())
  # print(*memoization(N))
  print(recursion_memoization(N))