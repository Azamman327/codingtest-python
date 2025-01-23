import sys

num = int(sys.stdin.readline())

def factorial(num):
  if num <= 1:
    return 1
  else:
    return num * factorial(num - 1)

print(factorial(num))