def remove_duplicates(arr):
  leftP, rightP = 0,1
  while rightP < len(arr):
    if (arr[leftP] == arr[rightP]):
      arr = arr[:leftP]+arr[rightP:]
    else:
      leftP += 1
      rightP += 1
  return len(arr)

arr = [2, 3, 3, 3, 6, 9, 9]
print(remove_duplicates(arr) == 4)

arr = [2, 2, 2, 11]
print(remove_duplicates(arr) == 2)