import sys
import itertools

n, m = list(map(int, sys.stdin.readline().split(' ')))
arr = list(map(int, sys.stdin.readline().split(' ')))

result = list(itertools.combinations(arr, 3))

maxnum = 0
for r in result:
  if sum(r) <= m:
    maxnum = max(maxnum, sum(r))

print(maxnum)
