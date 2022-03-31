from collections import deque

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class State:
  def __init__(self, curIndex, node):
    self.curIndex = curIndex
    self.node = node

def hasRight(node):
  return node.right != None

def hasLeft(node):
  return node.left != None

def isLeaf(node):
  return not hasLeft(node) and not hasRight(node)

def find_path(root, sequence):
  i = 0
  stack = deque()
  stack.append(State(i, root))
  while len(stack) > 0:
    curState = stack.pop()
    if(isLeaf(curState.node) and curState.curIndex == len(sequence)-1):
      return True
    if(hasLeft(curState.node) and 
      curState.curIndex < len(sequence)-1 and
      curState.node.left.val == sequence[curState.curIndex+1]
    ):
      stack.append(State(curState.curIndex+1, curState.node.left))
    if(hasRight(curState.node) and 
      curState.curIndex < len(sequence)-1 and
      curState.node.right.val == sequence[curState.curIndex+1]
    ):
      stack.append(State(curState.curIndex+1, curState.node.right))
  return False  


def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()