import itertools
import sys

n = int(sys.stdin.readline())
arr = [i for i in range(n)]
case = list(itertools.permutations(arr, 2))
print(len(case))

#그냥 수식으로
# import sys

# n = int(sys.stdin.readline())

# print(n * n - n)
