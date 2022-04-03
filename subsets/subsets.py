import copy


def find_subsets(nums):
  subsets = [[]]
  for num in nums:
    newSubsets = copy.deepcopy(subsets)
    for subset in subsets:
      subset.append(num)
      newSubsets.append(subset)
    subsets = newSubsets
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()