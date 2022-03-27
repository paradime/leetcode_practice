from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_sub_list(head, p, q):
  i = 1
  curNode = head
  while curNode != None:
    if(i == q):
      revStop = curNode.next
      break
    i += 1
    curNode = curNode.next
  
  i = 1
  curNode = head
  if p == 1:
    revMeta = reverseLLUntil(curNode, q-p)
    revMeta[1].next = revStop
    curNode = revMeta[0]
    return curNode
  while(curNode != None):
    if i+1 == p:
      revMeta = reverseLLUntil(curNode.next, q-p)
      curNode.next = revMeta[0]
      revMeta[1].next = revStop
      break
    i += 1
    curNode = curNode.next
  return head

def reverseLLUntil(head, stop):
  revHead = None
  i = 0
  revEnd = head
  while i <= stop:
    next = head.next
    head.next = revHead
    revHead = head
    head = next
    i+=1
  return [revHead, revEnd]

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()

  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 1, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()

main()
