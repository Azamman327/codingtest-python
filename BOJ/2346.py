from collections import deque
import sys

loop = int(sys.stdin.readline())

deq = deque()
deq = deque(map(int, sys.stdin.readline().rstrip().split(' ')))

memo = deque([i + 1 for i in range(len(deq))])

result = []

for i in range(loop):
  move = deq.popleft()
  balloon = memo.popleft()

  result.append(str(balloon))

  if move > 0:
    move = move - 1

  deq.rotate(move)
  memo.rotate(move)

print(" ".join(result))