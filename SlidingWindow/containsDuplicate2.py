from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      window = set()
      if k >= len(nums):
        for x in range(0, len(nums)):
          if nums[x] in window:
            return True
          window.add(nums[x])
        return False
      for x in range(0, k+1):
        if nums[x] in window:
          return True
        window.add(nums[x])
      for i in range(1, len(nums)-k):
        window.remove(nums[i-1])
        if nums[i+k] in window:
          return True
        window.add(nums[i+k])
      return False


nums = [1,2,3,1]
k = 3
print(Solution().containsNearbyDuplicate(nums, k) == True)

nums = [1,2,3,1]
k = 2
print(Solution().containsNearbyDuplicate(nums, k) == False)
nums = [1,0,1,1]
k = 1
print(Solution().containsNearbyDuplicate(nums, k) == True)

nums = [1,2,3,1,2,3]
k = 2
print(Solution().containsNearbyDuplicate(nums, k) == False)

nums = [1]
k = 2
print(Solution().containsNearbyDuplicate(nums, k) == False)

nums = [4,1,2,3,1,5]
k = 3
print(Solution().containsNearbyDuplicate(nums, k) == True)