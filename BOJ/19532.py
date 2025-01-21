import sys

a, b, c, d, e, f = list(map(int, sys.stdin.readline().rstrip().split(' ')))

for i in range(-999, 1000):
  for j in range(-999, 1000):
    if c == a*i + b*j and f == d*i + e*j:
      print(i, j)
