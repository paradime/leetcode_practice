import re
class Solution:
    def myAtoi(self, s: str) -> int:
      newString = s.strip()
      m = re.search('^[+-]?\d+', newString)
      if m:
        newInt = int(m.group(0))
        if newInt >= 2**31:
          return (2**31)-1
        elif newInt < -2**31:
          return -2**31
        return newInt
      return 0

s = "42"
print(Solution().myAtoi(s) == 42)
s = "   -42"
print(Solution().myAtoi(s) == -42)
s = "4193 with words"
print(Solution().myAtoi(s) == 4193)
s = "abc"
print(Solution().myAtoi(s) == 0)
s = "words and 987"
print(Solution().myAtoi(s) == 0)
s = "-91283472332"
print(Solution().myAtoi(s) == -2147483648)
s = "91283472332"
print(Solution().myAtoi(s) == 2147483647)
s = "2147483648"
print(Solution().myAtoi(s) == 2147483647)
s = "+-12"
print(Solution().myAtoi(s) == 0)