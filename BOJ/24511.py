import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split(' '))) # 0 큐 / 1 스택
b = deque(list(map(int, sys.stdin.readline().split(' '))))

m = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split(' ')))

blist = deque()

for i in range(n):
  if a[i] == 0:
    blist.append(b[i])

if not blist:
  print(' '.join(list(map(str, c))))
else:
  for i in range(m): 
    blist.appendleft(c[i])
    print(blist.pop(), end=' ')

# rslt = ''
# for i in range(m):
#   tmp = c[i]
#   for j in range(n - 1):
#     if a[j] == 0:
#       print(b)
#       tmp = b[j]
#       b[j] = c[i]

#   if a[-1] == 0:
#     rslt = rslt + str(b.pop()) + ' '
#     b.append(tmp)
#   else:
#     rslt = rslt + str(tmp) + ' '