def find_all_duplicates(nums):
  i = 0
  duplicates = []
  while i < len(nums):
    #i = current index
    #j = target index
    j = nums[i] -1
    if nums[i] == nums[j] and i != j:
      duplicates.append(nums[i])
      i +=1
    elif nums[i] == nums[j] and i == j:
      i +=1
    else:
      nums[i], nums[j] = nums[j], nums[i]
  return duplicates

nums = [3, 4, 4, 5, 5]
expected = [4,5]
print(find_all_duplicates(nums) == expected)

nums = [5, 4, 7, 2, 3, 5, 3]
expected = [3,5]
print(find_all_duplicates(nums) == expected)
