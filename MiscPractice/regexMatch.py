class Solution:
    def isMatch(self, s: str, p: str, log: bool = False) -> bool:
      if(len(p) == 0):
        return len(s) == 0
      firstMatch = (len(s) >0) and p[0] in {s[0], '.'}
      if(len(p) >= 2 and p[1] == "*"):# if more chars and on star
        noMoreStar = (self.isMatch(s, p[2:]))
        if noMoreStar:
          return noMoreStar
        if not firstMatch:
          return firstMatch
        moreStar = (self.isMatch(s[1:], p))
        return moreStar
      else:
        return firstMatch and self.isMatch(s[1:], p[1:]) # move onto next letter
      # if(len(p) > 1 and p[1] == "*"):
      #   return self.isMatchRecur(s, p, True, log)
      # return self.isMatchRecur(s, p, False, log)

    def isMatchRecur(self, s: str, p: str, star: bool, log: bool = False) -> bool:
      if(log):
        print("s: "+s)
        print("p: "+p)
        print("isStar: " +str(star))
      
      if(len(s) == 0 and star): # if no more in s, but in a star / missing 
        if(len(p)>2):
          return self.isMatch(s, p[2:], log)
        if(log):
          print("ending a: True")
        return True
      if(len(s) == 0 and len(p) > 0): # if no more in s, but maybe more stars in p
        if not star:
          return False
        if "*" in p:
          return self.isMatch(s, p[1:], log)
        return False
      if(len(p) == 1 and len(s) > 1): # if no star in p but more letters in S, no match
        if(log):
          print("ending b: False")
        return False
      if(len(s) == 0 and len(p) == 0): # if at the end of both
        if(log):
          print("ending c: True")
        return True
      if((s[0] == p[0] or p[0] == ".") and star == False): # compare letters
        return self.isMatch(s[1:], p[1:], log)
      if(((s[0] != p[0] or p[0] != ".") and star == False)):
        if(log):
          print("ending d: False")
        return False
      if(not star):
        return self.isMatchRecur(s[1:], p[1:], (len(p) > 2 and p[2] == "*"), log)
      # if this letter is *
      if(star):
        noMatch = self.isMatch(s, p[2:], log) if(len(p)>2) else False
        if noMatch:
          return noMatch
        if(s[0] == p[0] or p[0] == "."):
          noMoreStar = self.isMatch(s[1:], p[2:], log) if(len(p)>2) else False
          if noMoreStar:
            return noMoreStar
          MoreStar = self.isMatchRecur(s[1:], p, True, log) #no more and n more
          return MoreStar
        else:
          return noMatch
      
    # def isMatchRecur(self, s, p)
    def isMatch1(self, s: str, p: str) -> bool:
      match = True
      starMatch = True
      j = 0
      for i in range(0, len(p)):
        for j in range(i, len(s)):
          match = match and self.letterMatch(s, p, i, j) or self.starMatch(s,p,i,j)
          print(s[j] + p[i] + str(i) + str(j) + str(match))
          if(p[i] != "*"):
            if(not self.letterMatch(s,p,i,j)):
              return False
            if(len(p)-1 == i and len(s)-1 !=j): # if we are out of pattern and there are still more letters in s
              return False
            if(len(s)-1 == j and (len(p)-1 !=i and p[-1] != "*")):
              return False # if we are out of letters and there is still more pattern of letters
            else:
              break
          elif((not match) and self.starMatch(s,p,i,j) == False):
            match = True
            break
      return match

    def letterMatch(self, s, p, i, j):
      if(len(p)-1 == i):
        return s[j] == p[i] or p[i] == "."
      else:
        if s[j] == p[i]:
          return True 
        if p[i] == ".":
          return True
        if p[i+1] == "*":
          if(len(p)-1 < i+2):
            return False
          else:
            return self.letterMatch(s,p,i+2,j)

    def dotMatch(self, s, p, i, j):
      if(len(p)-1 == i):
        return p[i] == "."
      else:
        if p[i] == ".":
          return True 
        if p[i+1] == "*":
          if(len(p)-1 < i+2):
            return False
          else:
            return self.letterMatch(s,p,i+2,j)

    def starMatch(self, s, p, i, j):
      return (p[i] == "*") and self.letterMatch(s, p, i-1, j)

# letter
# star
# dot

s = "aa"
p = "a"
print(Solution().isMatch(s, p) == False)

s = "aa"
p = "a*"
print(Solution().isMatch(s, p) == True)

s = "aab"
p = "c*a*b"
print(Solution().isMatch(s, p) == True)
s = "mississippi"
p = "mis*is*p*."
print(Solution().isMatch(s, p) == False)
s = "mississippi"
p = "mis*is*ip*."
print(Solution().isMatch(s, p) == True)
s = "abcd"
p = "d*"
print(Solution().isMatch(s, p) == False)
s = "ab"
p = ".*c"
print(Solution().isMatch(s, p) == False)
s = "ab"
p = ".*"
print(Solution().isMatch(s, p) == True)
s="bbbba"
p=".*a*a"
print(Solution().isMatch(s, p) == True)
s="a"
p=".*..a*"
print(Solution().isMatch(s, p) == False)