# 중단한 문제
import sys
import copy

h, w = list(map(int, sys.stdin.readline().rstrip().split(' ')))

board = []
for i in range(h):
  line = list(sys.stdin.readline().rstrip())
  board.append(line)

original = copy.deepcopy(board)

minresult = 1000
cnt = 0

def changeBoard(i, j):
  if board[i][j] == 'B':
    if board[i][j] == board[i][j - 1]:
      board[i][j - 1] = 'W'
    elif board[i][j] == board[i][j + 1]:
      board[i][j + 1] = 'W'
    elif board[i][j] == board[i - 1][j]:
      board[i - 1][j] = 'W'
    elif board[i][j] == board[i + 1][j]:
      board[i + 1][j] = 'W'
  else:
    if board[i][j] == board[i][j - 1]:
      board[i][j - 1] = 'B'
    elif board[i][j] == board[i][j + 1]:
      board[i][j + 1] = 'B'
    elif board[i][j] == board[i - 1][j]:
      board[i - 1][j] = 'B'
    elif board[i][j] == board[i + 1][j]:
      board[i + 1][j] = 'B'


for i in range(h):
  for j in range(w):
    if i + 7 < h and j + 7 < w:
      for k in range(i + 8):
        for l in range(j + 8):
          if l + 1 >= w:
            break
          elif k + 1 >= h:
            break
          if board[k][l] == board[k][l - 1] or board[k][l] == board[k][l + 1] or board[k][l] == board[k - 1][l] or board[k][l] == board[k + 1][l]:
            cnt = cnt + 1
            changeBoard(k, l)
    if minresult > cnt:
      minresult = cnt
    # cnt = 0
    board = copy.deepcopy(original)

print(cnt)



        


