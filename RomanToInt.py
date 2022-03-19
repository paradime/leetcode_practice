class Solution:
    def romanToInt(self, s: str) -> int:
      count = 0
      skip = False
      for i in range(0, len(s)):
        if skip:
          skip = False
          continue
        letter = s[i]
        if(letter == "I"):
          if(i < len(s)-1 and s[i+1] == "V"):
            count += 4
            skip = True
          elif(i < len(s)-1 and s[i+1] == "X"):
            count += 9
            skip = True
          else:
            count += 1

        if(letter == "V"):
          count += 5

        if(letter == "X"):
          if(i < len(s)-1 and s[i+1] == "L"):
            count += 40
            skip = True
          elif(i < len(s)-1 and s[i+1] == "C"):
            count += 90
            skip = True
          else:
            count += 10 

        if(letter == "L"):
          count += 50 

        if(letter == "C"):
          if(i < len(s)-1 and s[i+1] == "D"):
            count += 400
            skip = True
          elif(i < len(s)-1 and s[i+1] == "M"):
            count += 900
            skip = True
          else:
            count += 100 

        if(letter == "D"):
          count += 500 

        if(letter == "M"):
          count += 1000
      return count


s = "III"
print(Solution().romanToInt(s) == 3)
s = "IV"
print(Solution().romanToInt(s) == 4)
s = "IX"
print(Solution().romanToInt(s) == 9)
s = "LVIII"
print(Solution().romanToInt(s) == 58)
s = "MCMXCIV"
print(Solution().romanToInt(s) == 1994)