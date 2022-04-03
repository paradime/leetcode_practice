import copy


def find_subsets(nums):
  subsets = [[]]
  nums.sort()
  lastAdded = []
  lastSeen = nums[0] -1
  for num in nums:
    newSubsets = copy.deepcopy(subsets)
    tempLastAdded = list(lastAdded)
    lastAdded = []
    if num == lastSeen:
      for subset in tempLastAdded:
        subset.append(num)
        newSubsets.append(subset)
        lastAdded.append(subset)
    else:
      for subset in subsets:
        subset.append(num)
        newSubsets.append(subset)
        lastAdded.append(subset)
    subsets = newSubsets
    lastSeen = num
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
