from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      if len(s) == 0:
        return 0
      return self.lengthOfLongestSubstringRecur(s, [], [])

    def lengthOfLongestSubstringRecur(self, s: str, listOfSetNoDupes:list[set], listOfSetFoundDupes:list[set]):
      newListOfSetNoDupes = []
      if(len(s) == 0):
        return len(max(listOfSetNoDupes+listOfSetFoundDupes, key = lambda x: len(x)))
      for letters in listOfSetNoDupes:
        if s[0] in letters:
          listOfSetFoundDupes.append(letters)
        else:
          letters.add(s[0])
          newListOfSetNoDupes.append(letters)
      newListOfSetNoDupes.append({s[0]})
      return self.lengthOfLongestSubstringRecur(s[1:], newListOfSetNoDupes, listOfSetFoundDupes)
d = {}
print(set().union([1,3],[2]))
listOfDict = [{'a', 1}, {}]
print(len(max((listOfDict+ [{1}]), key = lambda x: len(x))))
s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s)== 3)
s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s)== 1)
s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s)== 3)
s = ""
print(Solution().lengthOfLongestSubstring(s)== 0)

