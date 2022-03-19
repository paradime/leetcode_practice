class Solution:
    def intToRoman(self, num: int) -> str:
      curNum = num
      roman = ""
      table = [
        ["M", 1000],
        ["CM", 900],
        ["D", 500],
        ["CD", 400],
        ["C", 100],
        ["XC", 90],
        ["L", 50],
        ["XL", 40],
        ["X", 10],
        ["IX", 9],
        ["V", 5],
        ["IV", 4],
        ["I", 1]
      ]
      while(curNum > 0):
        for conversion in table:
          if curNum / conversion[1] >= 1:
            roman += conversion[0]
            curNum -= conversion[1]
            break
      return roman

n = 1
print(Solution().intToRoman(n)=="I")
n = 4
print(Solution().intToRoman(n)=="IV")
n = 5
print(Solution().intToRoman(n)=="V")
n = 3
print(Solution().intToRoman(n)=="III")
n = 58
print(Solution().intToRoman(n)=="LVIII")
n = 1994
print(Solution().intToRoman(n)=="MCMXCIV")
n = 3999
print(Solution().intToRoman(n)=="MMMCMXCIX")