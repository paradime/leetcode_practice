from collections import deque


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class State:
  def __init__(self, stringRep, node):
    self.stringRep = stringRep
    self.node = node

def hasRight(node):
  return node.right != None

def hasLeft(node):
  return node.left != None

def isLeaf(node):
  return not hasRight(node) and not hasLeft(node)

def find_sum_of_path_numbers(root):
  stack = deque()
  stack.append(State("", root))
  sum = 0
  while len(stack) > 0:
    curState = stack.pop()
    if isLeaf(curState.node):
      sum += int(curState.stringRep + str(curState.node.val))
    if hasLeft(curState.node):
      stack.append(State(curState.stringRep + str(curState.node.val), curState.node.left))
    if hasRight(curState.node):
      stack.append(State(curState.stringRep + str(curState.node.val), curState.node.right))
  return sum



def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()