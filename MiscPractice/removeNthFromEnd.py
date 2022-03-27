# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      llLength = lenOfLL(head)
      i = 0
      newHead = ListNode()
      newHead.next = head
      curNode = newHead
      while i < llLength-n:
        i+=1
        curNode = curNode.next
      curNode.next = curNode.next.next
      return newHead.next

def lenOfLL(head):
  curNode = head
  i = 0
  while(curNode != None):
    i += 1
    curNode = curNode.next
  return i

def printLL(head):
  listVersion = []
  curNode = head
  while(curNode != None):
    listVersion.append(curNode.val)
    curNode = curNode.next
  print(listVersion)

head = ListNode(val= 1)
head.next = ListNode(val = 2)
head.next.next = ListNode(val = 3)
head.next.next.next = ListNode(val = 4)
head.next.next.next.next = ListNode(val = 5)
#print(lenOfLL(head))
newHead = Solution().removeNthFromEnd(head, 2)
printLL(newHead)

head = ListNode(val= 1)
newHead = Solution().removeNthFromEnd(head, 1)
printLL(newHead)

head = ListNode(val= 1)
head.next = ListNode(val = 2)
newHead = Solution().removeNthFromEnd(head, 1)
printLL(newHead)

head = ListNode(val= 1)
head.next = ListNode(val = 2)
newHead = Solution().removeNthFromEnd(head, 2)
printLL(newHead)