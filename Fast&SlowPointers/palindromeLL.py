from sympy import false


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def printLL(head):
  pointer = head
  while pointer!= None:
    print(pointer.value)
    pointer = pointer.next

def is_palindromic_linked_list(head):
  # find the middle
  listLength = lengthOf(head)
  middleIndex = int(listLength/2)-1 if listLength%2 == 0 else int(listLength/2)
  middleNode = nodeAt(middleIndex, head)

  # reverse second half
  middleNode.next= reverseLL(middleNode.next)

  # setup pointers
  rightNode = middleNode.next
  leftNode = head
  # compare first half to second half
  isPalin = True
  while rightNode != None:
    if rightNode.value != leftNode.value:
      isPalin = False
    rightNode = rightNode.next
    leftNode = leftNode.next

  #reverse again
  middleNode.next = reverseLL(middleNode.next)
  return isPalin

def reverseLL(head):
  prev = None
  while(head != None):
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev

def is_palindromic_linked_list_mine(head):
  listLength = lengthOf(head)
  middleIndex = int(listLength/2)
  slowStartIndex = middleIndex
  if listLength % 2 == 0:
    fastStartIndex = middleIndex - 1
  else:
    fastStartIndex = middleIndex
  slowStartNode = nodeAt(slowStartIndex, head)
  fastStartNode = nodeAt(fastStartIndex, head)
  while slowStartNode != None:
    if slowStartNode.value != fastStartNode.value:
      return False
    slowStartIndex += 1
    fastStartIndex -= 1
    slowStartNode = nodeAt(1, slowStartNode)
    fastStartNode = nodeAt(fastStartIndex, head)
  return True


def nodeAt(index, head):
  i = 0
  pointer = head
  while(i < index):
    pointer = pointer.next
    i +=1
  return pointer

def lengthOf(head):
  index = 0
  pointer = head
  while pointer != None:
    pointer = pointer.next
    index += 1
  return index

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(6)
  head.next.next.next.next = Node(4)
  head.next.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
