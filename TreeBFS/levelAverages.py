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

def find_level_averages(root):
  result = []
  queue = [MatrixLoc(node=root, level=0)]
  while(len(queue) != 0):
    item = queue.pop(0)
    if(len(result) <= item.level):
      result.append([])
    result[item.level].append(item.node.val)
    if item.node.left:
      queue.append(MatrixLoc(node=item.node.left, level=item.level+1))
    if item.node.right:
      queue.append(MatrixLoc(node=item.node.right, level=item.level+1))
  res2 = []
  for level in result:
    res2.append(sum(level)/len(level))
  return res2


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))



main()