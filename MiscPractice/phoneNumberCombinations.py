from typing import List
from functools import reduce
from itertools import chain


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
      if len(digits) == 0:
        return []
      combinations = []
      letterMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
      }

      combinations = self.letterCombinationsRecurs(digits, letterMap, "")
      return self.flatten(combinations)
    
    def flatten(self, combinations):
      if isinstance(combinations[0], str):
        return combinations
      newList = list(chain.from_iterable(combinations))
      return self.flatten(newList)

    def letterCombinationsRecurs(self, digits, letterMap, acc):
      combinations = []
      
      if len(digits) < 1:
        return acc

      curDigit = digits[0]

      for l in letterMap[curDigit]:
        combinations.append(self.letterCombinationsRecurs(digits[1:], letterMap, acc + l))
      return combinations

digits = ""
print(Solution().letterCombinations(digits)== [])
digits = "2"
print(Solution().letterCombinations(digits) == ["a","b","c"])
digits = "23"
print(Solution().letterCombinations(digits) == ["ad","ae","af","bd","be","bf","cd","ce","cf"])