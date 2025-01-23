import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split(' ')))

a = []
num = list(map(int, sys.stdin.readline().rstrip().split(' ')))
for i in range(n):
  if num[i] < m:
    a.append(str(num[i]))

print(' '.join(a)) 