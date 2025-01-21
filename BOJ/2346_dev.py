# enumerate 사용 (index, element) 짝지어져 저장됨
from collections import deque
import sys

loop = int(sys.stdin.readline())

deq = deque(enumerate(map(int, sys.stdin.readline().rstrip().split(' '))))

result = []
for i in range(loop):
  idx, move = deq.popleft()
  result.append(idx + 1)

  # 음수: 왼쪽으로 회전, 양수: 오른쪽으로 회전
  # 음수: [3, 4, 5, 6, 7, 8, 9, 1, 2]
  # 양수: [8, 9, 1, 2, 3, 4, 5, 6, 7]
  if move > 0:
    deq.rotate(-(move - 1))
  else:
    deq.rotate(-move)

print(' '.join(map(str, result)))