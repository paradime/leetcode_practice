def smallest_subarray_sum(s, arr):
  minLen = -1 
  i, j = 0,0
  sum = arr[i]
  while i< len(arr):
    if sum < s and j < len(arr)-1:
      j+=1
      sum += arr[j]
    elif sum >= s:
      if minLen == -1 or j-i < minLen:
        minLen = j-i+1
      sum -= arr[i]
      i+=1
    else:
      sum -= arr[i]
      i+=1
  return minLen


arr = [2, 1, 5, 2, 3, 2]
S=7 
print(smallest_subarray_sum(S, arr) == 2)

arr = [2, 1, 5, 2, 8]
S=7 
print(smallest_subarray_sum(S, arr) == 1)

arr = [3, 4, 1, 1, 6]
S=8
print(smallest_subarray_sum(S, arr) == 3)