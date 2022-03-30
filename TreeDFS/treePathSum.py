from collections import deque


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class State:
  def __init__(self, curSum, node, path):
    self.curSum = curSum
    self.node = node
    self.path = path

def hasRight(node):
  return node.right != None

def hasLeft(node):
  return node.left != None

def isLeaf(node):
  return not hasRight(node) and not hasLeft(node)

def find_paths(root, s):
  sum = 0
  stack = deque()
  stack.append(State(sum, root, []))
  paths = []
  while (len(stack) > 0):
    curState = stack.pop()
    sum = curState.node.val + curState.curSum
    newP = list(curState.path)
    newP.append(curState.node.val)
    if isLeaf(curState.node):
      if s == sum:
        paths.append(newP)
    if hasLeft(curState.node):
      stack.append(State(sum, curState.node.left, newP))
    if hasRight(curState.node):
      stack.append(State(sum, curState.node.right, newP))
  return paths

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths with required_sum " + str(required_sum) +
        ": " + str(find_paths(root, required_sum)))


main()