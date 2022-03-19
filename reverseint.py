class Solution:
    def reverse(self, x: int) -> int:
      isNegative = False
      newInt = x
      if x < 0:
        newInt *= -1
        isNegative = True
      newInt = int(str(newInt)[::-1]) * (-1 if isNegative else 1)
      if newInt < -2**31 or newInt > 2**31 -1:
        return 0
      return newInt

x = 123
print(Solution().reverse(x) == 321)
x = -123
print(Solution().reverse(x) == -321)
x = 120
print(Solution().reverse(x) == 21)
x = 1534236469
print(Solution().reverse(x) == 0)
