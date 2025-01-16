import sys

stack = []
sentence = sys.stdin.readline().rstrip()
result = "yes"

def find(word):
  if word == '(' or word == '[':
    stack.append(word)
  elif word == ')':
    if stack != [] and stack[-1] == '(':
      stack.pop()
    else:
      return False
  elif word == ']':
    if stack != [] and stack[-1] == '[':
      stack.pop()
    else:
      return False

while sentence != '.':
  for word in sentence:
    if (find(word) == False):
      result = "no"
      break
  
  if stack == []:
    print(result)
  else:
    print("no")

  sentence = sys.stdin.readline().rstrip()
  result = "yes"
  stack.clear()
