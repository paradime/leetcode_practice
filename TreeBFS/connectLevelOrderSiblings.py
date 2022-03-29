from collections import deque
from dataclasses import dataclass


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None
    self.next = None

    # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()

@dataclass
class MatrixLoc:
  node: TreeNode
  level: int

def traverse(root):
  result = []
  queue = [MatrixLoc(node=root, level=0)]
  while(len(queue) != 0):
    item = queue.pop(0)
    if(len(result) <= item.level):
      result.append([])
    result[item.level].append(item.node)
    if item.node.left:
      queue.append(MatrixLoc(node=item.node.left, level=item.level+1))
    if item.node.right:
      queue.append(MatrixLoc(node=item.node.right, level=item.level+1))
  return result

def connect_level_order_siblings(root):
  arrInterp = traverse(root)
  for row in arrInterp:
    for i in range(len(row)-1):
      row[i].next = row[i+1]
  return arrInterp[0][0]
      


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_level_order_siblings(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()


main()