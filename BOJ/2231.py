import sys

n = int(sys.stdin.readline())

result = 0

for i in range(1, n):
  if n == i + sum(list(map(int, str(i)))):
    result = i
    break

print(result)