import sys

cnt = 0

def recursion(s, l, r):
  global cnt
  cnt += 1
  if l >= r:
    return 1
  elif s[l] != s[r]:
    return 0
  else:
    return recursion(s, l + 1, r - 1)

def isPalindrome(s):
  global cnt
  cnt = 0
  return recursion(s, 0, len(s) - 1)

n = int(sys.stdin.readline())
for i in range(n):
  s = sys.stdin.readline().rstrip()
  result = isPalindrome(s)
  print(result, cnt)