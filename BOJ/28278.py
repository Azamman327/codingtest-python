import sys

loop = int(sys.stdin.readline())

stack=[]

def isNull():
  if stack == []:
    return True
  return False

def push():
  stack.append(action.split(' ')[1])

def pop():
  if isNull():
    print(-1)
  else:
    a = stack.pop()
    print(a)

def length():
  print(len(stack))

def get():
  if isNull():
    print(-1)
  else:
    print(stack[-1])

for i in range(loop):
  action = sys.stdin.readline().rstrip()
    
  if action.split(' ')[0] == '1':
    push()
    
  elif action == '2':
    pop()

  elif action == '3':
    length()

  elif action == '4':
    if isNull():
      print(1)
    else:
      print(0)

  elif action == '5':
    get()
