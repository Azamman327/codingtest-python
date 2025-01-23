import sys

loop = int(sys.stdin.readline())

for i in range(loop):
  a = list(sys.stdin.readline().rstrip())
  sum = 0
  cnt = 1
  for j in a:
    if j == 'O':
      sum += cnt
      cnt += 1
    else:
      cnt = 1
  print(sum)