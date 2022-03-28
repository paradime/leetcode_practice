def binary_search(arr, key):
  if isAscending(arr):
    return binary_search_asc(arr, key)
  else:
    return binary_search_desc(arr, key)

def isAscending(arr):
  if (arr[0] < arr[-1]):
    return True

def binary_search_asc(arr, key):
  firstIndex = 0
  lastIndex = len(arr)-1
  middleIndex = int((lastIndex-firstIndex)/2)
  pivot = arr[middleIndex]
  if pivot == key:
    return middleIndex
  while firstIndex != lastIndex:
    if pivot < key:
      firstIndex = middleIndex+1
      middleIndex = firstIndex+int((lastIndex-firstIndex)/2)
      pivot = arr[middleIndex]
    elif key < pivot:
      lastIndex = middleIndex
      middleIndex = int((lastIndex-firstIndex)/2)
      pivot = arr[middleIndex]
    if pivot == key:
      return middleIndex
  return -1

def binary_search_desc(arr, key):
  firstIndex = 0
  lastIndex = len(arr)-1
  middleIndex = int((lastIndex-firstIndex)/2)
  pivot = arr[middleIndex]
  if pivot == key:
    return middleIndex
  while firstIndex != lastIndex:
    if pivot > key:
      firstIndex = middleIndex+1
      middleIndex = firstIndex+int((lastIndex-firstIndex)/2)
      pivot = arr[middleIndex]
    elif key > pivot:
      lastIndex = middleIndex
      middleIndex = int((lastIndex-firstIndex)/2)
      pivot = arr[middleIndex]
    if pivot == key:
      return middleIndex
  return 0

def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()