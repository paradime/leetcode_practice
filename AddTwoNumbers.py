from typing import Optional;
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      return self.addTwoNumbersRecur(l1, l2, 0)

    def addTwoNumbersRecur(self, l1: Optional[ListNode], l2: Optional[ListNode], carry) -> Optional[ListNode]:
      if l1 == None and l2 == None:
        if carry > 0:
          return ListNode(carry, None)
        return None
      if l1 == None:
        sum = l2.val + carry
        return ListNode(sum % 10, self.addTwoNumbersRecur(l1, l2.next, 1 if sum >= 10 else 0))
      if l2 == None:
        sum = l1.val + carry
        return ListNode(sum % 10, self.addTwoNumbersRecur(l1.next, l2, 1 if sum >= 10 else 0))
      sum = l1.val + l2.val + carry
      return ListNode(sum % 10, self.addTwoNumbersRecur(l1.next, l2.next, 1 if sum >= 10 else 0))


def convertToListNodes(arr):
  if len(arr) == 0:
    return None
  return ListNode(arr[0], convertToListNodes(arr[1:]))

print(Solution().addTwoNumbers(convertToListNodes([2,4,3]), convertToListNodes([5,6,4])))

# print(Solution().addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))