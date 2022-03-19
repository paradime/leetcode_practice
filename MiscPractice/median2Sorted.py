from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l3 = self.merge(nums1, nums2)
        if len(l3) % 2== 0:
            return (l3[int(len(l3)/2)-1] + l3[int(len(l3)/2)])/2
        return l3[int(len(l3)/2)]

    def merge(self, nums1, nums2):
      l3 = []
      if len(nums1) > len(nums2):
        longest = nums1
        shortest = nums2
      else:
        longest = nums2
        shortest = nums1
      j = 0
      i = 0
      while i < len(longest) or j < len(shortest):
        if i == len(longest):
          l3.append(shortest[j])
          j += 1
        elif j == len(shortest):
          l3.append(longest[i])
          i += 1
        elif longest[i] < shortest[j]:
          l3.append(longest[i])
          i += 1
        else:
          l3.append(shortest[j])
          j += 1
      return l3




nums1 = [1,2]
nums2 = [3,4]
print(Solution().findMedianSortedArrays(nums1, nums2))