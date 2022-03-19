class Solution:
    def convert(self, s: str, numRows: int) -> str:
      if numRows == 1:
        return s
      newWord = ""
      for i in range(0, numRows):
        ci = i
        if(i % numRows == 0 or i % numRows == numRows-1):
          while ci < len(s):
            newWord += s[ci]
            ci += (numRows+(numRows-2))
        else:
          while ci < len(s):
            newWord += s[ci]
            newlimit = (numRows-2)*2 - (2*(i-1))
            ci += newlimit
            if ci >= len(s):
              break
            newWord += s[ci]
            ci += (numRows+(numRows-2)-newlimit)
      return newWord
      # arr2d = []
      # for i in range(0, numRows):
      #   arr2d.append([])
      # ci = 0
      # row = 0
      # while ci < len(s):
      #   for i in range(0, numRows):
      #     if row % (numRows-1) == 0:
      #       arr2d[i].append(s[ci])
      #       ci += 1
      #       if ci == len(s):
      #         break
      #     elif ((numRows-1) - (row % (numRows-1))) == i:
      #       arr2d[i].append(s[ci])
      #       ci += 1
      #       if ci == len(s):
      #         break
      #     else:
      #       arr2d[i].append("")
      #   row += 1
      # newWord = ""
      # for i in range(0, numRows):
      #   for letter in arr2d[i]:
      #     if(letter != ""):
      #       newWord+= letter
      # return newWord
    

s = "PAYPALISHIRING"
numRows = 3
print(Solution().convert(s, numRows) == "PAHNAPLSIIGYIR")
s = "PAYPALISHIRING"
numRows = 4
print(Solution().convert(s, numRows) == "PINALSIGYAHRPI")
s = "A"
numRows = 1
print(Solution().convert(s, numRows) == "A")
s = ""
numRows = 1
print(Solution().convert(s, numRows) == "")