import sys

loop = int(sys.stdin.readline())

stack = []
for i in range(loop):
  number = int(sys.stdin.readline())

  if number == 0:
    stack.pop()
  else:
    stack.append(number)

print(sum(stack))
