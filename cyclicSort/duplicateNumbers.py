def find_duplicate(nums):
  i = 0
  while i < len(nums):
    j = nums[i]
    if nums[i] == nums[j] and nums[i] != i+1:
      return nums[i]
    elif nums[i] != nums[j] and nums[i] == i+1:
      i +=1
    else:
      nums[i], nums[j] = nums[j], nums[i]
  return -1

nums = [1, 4, 4, 3, 2]
expected = 4
print(find_duplicate(nums) == expected)

nums = [2, 1, 3, 3, 5, 4]
expected = 3
print(find_duplicate(nums) == expected)

nums = [2, 4, 1, 4, 4]
expected = 4
print(find_duplicate(nums) == expected)