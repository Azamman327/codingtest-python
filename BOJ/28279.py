import sys
from collections import deque

loop = int(sys.stdin.readline())

deq = deque()
for i in range(loop):
  command = sys.stdin.readline().rstrip()
  if command.startswith('1') or command.startswith('2'):
    command, num = list(map(int, command.split(' ')))
  else:
    command = int(command)

  if 1 == command:
    deq.appendleft(num)
  elif 2 == command:
    deq.append(num)
  elif 3 == command:
    if deq:
      print(deq.popleft())
    else:
      print(-1)
  elif 4 == command:
    if deq:
      print(deq.pop())
    else:
      print(-1)
  elif 5 == command:
    print(len(deq))
  elif 6 == command:
    if deq:
      print(0)
    else:
      print(1)
  elif 7 == command:
    if deq:
      print(deq[0])
    else:
      print(-1)
  elif 8 == command:
    if deq:
      print(deq[-1])
    else:
      print(-1)