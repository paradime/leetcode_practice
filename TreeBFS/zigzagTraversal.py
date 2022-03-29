from collections import deque
from dataclasses import dataclass


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

@dataclass
class MatrixLoc:
  def __init__(self, node, level):
    self.node = node
    self.level = level

def traverse(root):
  result = []
  queue = [MatrixLoc(node=root, level=0)]
  while(len(queue) != 0):
    item = queue.pop(0)
    if(len(result) <= item.level):
      result.append([])
    if item.level % 2 == 1:
      result[item.level].insert(0,item.node.val)
    else:
      result[item.level].append(item.node.val)
    if item.node.left:
      queue.append(MatrixLoc(node=item.node.left, level=item.level+1))
    if item.node.right:
      queue.append(MatrixLoc(node=item.node.right, level=item.level+1))
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()