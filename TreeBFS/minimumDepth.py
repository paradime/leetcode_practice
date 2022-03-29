from collections import deque
from dataclasses import dataclass


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

class MatrixLoc:
  def __init__(self, node, level):
    self.node = node
    self.level = level

def find_minimum_depth(root):
  queue = [MatrixLoc(node=root, level=0)]
  while(len(queue) != 0):
    item = queue.pop(0)
    if not item.node.left and not item.node.right:
      return item.level+1
    if item.node.left:
      queue.append(MatrixLoc(node=item.node.left, level=item.level+1))
    if item.node.right:
      queue.append(MatrixLoc(node=item.node.right, level=item.level+1))


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()