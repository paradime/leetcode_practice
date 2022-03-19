class Solution:
    def isValid(self, s: str) -> bool:
      stack  = []
      for c in s:
        opposite = ''
        if c == ')':
          opposite = '('
        if c == ']':
          opposite = '['
        if c == '}':
          opposite = '{'
          
        if c in ['(','[','{']:
          stack.append(c)
        elif len(stack) == 0:
          return False
        elif stack[-1] == opposite:
          stack.pop()
        else:
          return False
      return len(stack) == 0

s = "()"
print(Solution().isValid(s) == True)

s = "()[]{}"
print(Solution().isValid(s) == True)

s = "(]"
print(Solution().isValid(s) == False)
s= "]"
print(Solution().isValid(s) == False)