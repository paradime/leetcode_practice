def cyclic_sort(nums):
  i = 0
  while i < len(nums):
    if i == nums[i]-1: # correct spot
      i+=1
    else:
      swap(nums, i, nums[i]-1)
  return nums

def swap(nums, i, j):
  nums[i], nums[j] = nums[j], nums[i]

a = [3, 1, 5, 4, 2]
print(cyclic_sort(a) == [1,2,3,4,5])