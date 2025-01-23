import sys

loop = int(sys.stdin.readline())

for i in range(loop):
  l = list(map(int, sys.stdin.readline().rstrip().split(' ')))
  n = l.pop(0)

  cnt = 0
  for a in l:
    avg = sum(l) // n
    if a > avg:
      cnt += 1

  answer = format(round(cnt / n * 100, 3), '.3f')
  print(f'{answer}%')