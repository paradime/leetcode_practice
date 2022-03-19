def pair_with_targetsum(arr, target_sum):
  firstPoint, lastPoint = 0, len(arr) -1
  while(firstPoint != lastPoint):
    firstVal = arr[firstPoint]
    lastVal = arr[lastPoint]
    firstComplement = target_sum-firstVal
    if(firstComplement == lastVal):
      return [firstPoint, lastPoint]
    elif(firstComplement < lastVal):
      lastPoint -= 1
    else:
      firstPoint += 1
  return [-1, -1]

arr = [1, 2, 3, 4, 6]
target=6
print(pair_with_targetsum(arr, target) == [1,3])

arr = [2, 5, 9, 11]
target=11
print(pair_with_targetsum(arr, target) == [0,2])

arr = [2,3]
target=11
print(pair_with_targetsum(arr, target) == [-1,-1])

arr = [1,3,7]
target=6
print(pair_with_targetsum(arr, target) == [-1,-1])