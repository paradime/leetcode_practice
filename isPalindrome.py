class Solution:
    def isPalindrome(self, x: int) -> bool:
      return str(x) == str(x)[::-1]

print(Solution().isPalindrome(121) == True)
print(Solution().isPalindrome(123) == False)
print(Solution().isPalindrome(10) == False)
print(Solution().isPalindrome(-101) == False)