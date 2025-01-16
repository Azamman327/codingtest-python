

def merge(a, left, right):
  sorted = []
  mid = (left + right) // 2
  i, j = left, mid + 1

  while i <= mid and j <= right:
    if a[i] <= a[j]:
      sorted.append(a[i])
      i += 1
    else:
      sorted.append(a[j])
      j += 1
  
  while i <= mid:
    sorted.append(a[i])
    i += 1

  while j <= right:
    sorted.append(a[j])
    j += 1
  
  for k in range(left, right + 1):
    a[k] = sorted[k - left]
  return a

def merge_sort(a, left, right):
  if left >= right:
    return
  
  mid = (left + right) // 2 # 중간 지점 찾아서
  merge_sort(a, left, mid) # 또 반을 나누기(왼쪽)
  merge_sort(a, mid + 1, right) # 또 반을 나누기(오른쪽)

  sorted_array = merge(a, left, right)
  return sorted_array

i = 0
n = 7
a = [21, 10, 12, 20, 25, 13, 15]

print(merge_sort(a, 0, n-1))