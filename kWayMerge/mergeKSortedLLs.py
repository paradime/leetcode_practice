from __future__ import print_function
from heapq import *


class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None


def merge_lists(heads):
  sortedHead = None
  minHeap = []
  for i in range(len(heads)):
    heappush(minHeap, (heads[i].value, i))
  
  print(minHeap)
  
  while len(minHeap) > 0:
    # val, listIndex
    record = heappop(minHeap)
    
    #append val to LL
    newNode = ListNode(record[0])
    if sortedHead == None:
      sortedHead = newNode
      curNode = newNode
    else:
      curNode.next = newNode
      curNode = curNode.next
    
    # push next val in list to heap
    heads[record[1]] = heads[record[1]].next
    if heads[record[1]] != None:
      heappush(minHeap, (heads[record[1]].value, record[1]))
  return sortedHead

def main():
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)

  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result != None:
    print(str(result.value) + " ", end='')
    result = result.next


main()