def find_missing_number(nums):
  # seen = set()
  # for num in nums:
  #   seen.add(num)
  cyclic_sort(nums)
  for i in range(len(nums)):
    if nums[i]!= i:
      return i
  return -1

def cyclic_sort(nums):
  i = 0
  while i < len(nums):
    j = nums[i]
    if nums[i] < len(nums) and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
  return nums


nums = [4,0,3,1]
missing = 2
print(cyclic_sort(nums))
print(find_missing_number(nums) == missing)

nums = [8, 3, 5, 2, 4, 6, 0, 1]
missing = 7
print(cyclic_sort(nums))
print(find_missing_number(nums) == missing)