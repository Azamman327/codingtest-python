import sys
loop = int(sys.stdin.readline())

stack = list(map(int, sys.stdin.readline().split(' ')))
temp = []
result = []

count = 0
flag = True
while stack != [] or temp != []:
  if stack != [] and stack[0] == count + 1: #stack에 일치하는 게 있다면
    result.append(stack.pop(0))
    count += 1
  elif temp != [] and temp[0] == count + 1: # temp에 일치하는 게 있다면
    result.append(temp.pop(0))
    count += 1
  elif stack != []:
    temp.insert(0, stack.pop(0))
  else:
    print("Sad")
    flag = False
    break

if (flag):
  print("Nice")



