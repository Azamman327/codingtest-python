import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split(' ')))
a = [int(x) for x in sys.stdin.readline().rstrip().split(' ')]

for i in range(n):
  if a[i] < m:
    print(a[i], end=' ')