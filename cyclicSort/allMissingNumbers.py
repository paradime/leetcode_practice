def find_missing_numbers(nums):
  missingNumbers = []
  cyclic_sort(nums)
  for x in range(1, len(nums)+1):
    if nums[x-1] != x:
      missingNumbers.append(x)
  return missingNumbers

def cyclic_sort(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != i and nums[j] != nums[i]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
  return nums


nums = [2, 3, 1, 8, 2, 3, 5, 1]
missingNums = [4, 6, 7]
print(find_missing_numbers(nums))# == missingNums)

nums = [2, 4, 1, 2]
missingNums = [3]
print(find_missing_numbers(nums))# == missingNums)

nums = [2, 3, 2, 1]
missingNums = [4]
print(find_missing_numbers(nums))# == missingNums)