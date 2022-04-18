import copy
from typing import List


def find_subsets(nums):
  subsets = [[]]
  for num in nums:
    newSubsets = copy.deepcopy(subsets)
    for subset in subsets:
      subset.append(num)
      newSubsets.append(subset)
    subsets = newSubsets
  return subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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

  print("Here is the list of subsets: " + str(Solution().subsets([1, 3])))
  print("Here is the list of subsets: " + str(Solution().subsets([1, 5, 3])))


main()