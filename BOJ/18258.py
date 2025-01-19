# 일반 pop()연산은 O(n)이고 deque의 popleft()는 O(1)이라서 deque 쓰는게 더 빠르다
import sys
from collections import deque

loop = int(sys.stdin.readline())
deq = deque()

# queue = []
for i in range(loop):
  command = sys.stdin.readline().rstrip()
  
  if command.startswith("push"):
    command = command.split(" ")
    deq.append(int(command[1]))
    continue

  elif command == "pop":
    if not deq:
      print(-1)
    else:
      print(deq.popleft())
    continue

  elif command == "size":
    print(len(deq))
    continue

  elif command == "empty":
    if not deq:
      print(1)
    else:
      print(0)
    continue

  elif command == "front":
    if not deq:
      print(-1)
    else:
      print(deq[0])
    continue

  elif command == "back":
    if not deq:
      print(-1)
    else:
      print(deq[-1])
    continue