# enumerate 사용
from collections import deque
import sys

loop = int(sys.stdin.readline())

deq = deque(enumerate(map(int, sys.stdin.readline().rstrip().split(' '))))

result = []
for i in range(loop):
  idx, move = deq.popleft()
  result.append(idx + 1)

  if move > 0:
    deq.rotate(-(move - 1))
  else:
    deq.rotate(-move)

print(' '.join(map(str, result)))