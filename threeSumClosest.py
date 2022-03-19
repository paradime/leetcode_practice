from typing import List
import time


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
      closest = 10**5

      for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):

          for k in range(j+1, len(nums)):
            s = sum([nums[i], nums[j], nums[k]])
            if self.isCloser(closest, target, s):
              closest = s
            if target - closest ==  0:
              return closest

      return closest
    

    def isCloser(self, curClosest, target, testSum):
      return abs(target -testSum) < abs(target - curClosest)




nums = [0,0,0]
target = 1
print(Solution().threeSumClosest(nums, target) == 0)
nums = [0,1,0]
target = 1
print(Solution().threeSumClosest(nums, target) == 1)
nums = [0,1,1]
target = 1
print(Solution().threeSumClosest(nums, target) == 2)
nums = [-1,2,1,-4]
target = 1
print(Solution().threeSumClosest(nums, target) == 2)

tic = time.perf_counter()
nums = [-10,-82,-70,92,39,-98,94,93,27,-74,1,-80,-95,-36,10,-12,43,92,-61,30,-26,100,-35,-54,-91,-58,-73,-66,86,8,1,49,-46,55,-89,39,45,66,96,42,80,-76,-69,53,-75,16,-13,53,-37,98,-59,72,41,-50,-23,-21,91,22,4,-80,1,-89,93,5,82,20,5,-77,95,16,-51,-21,0,-66,-84,-17,6,-65,12,94,-38,1,71,23,-71,50,8,28,80,-47,5,-13,69,-9,13,41,83,-61,-87,-51,89,-10,37,-73,-64,11,49]
target = 215
print(Solution().threeSumClosest(nums, target) == 215)
toc = time.perf_counter()
print(f"Completed in {toc - tic:0.4f} seconds")