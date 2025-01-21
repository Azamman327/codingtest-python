import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split(' '))

deq = deque([i + 1 for i in range(n)]) 
result = deque()


while len(deq) != 0:
  deq.rotate(-(k - 1))
  result.append(deq.popleft())

print('<', end="")
for i in range(len(result) - 1):
  print(result[i], end=", ")
print(result[-1], end="")
print('>', end="")
