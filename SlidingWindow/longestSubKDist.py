def longest_substring_with_k_distinct(str1, k):
  letterTally = {}
  windowStart, windowEnd = 0, 0
  maxLen = -1
  tempLen = 0
  while windowStart < len(str1):
    if (windowEnd == len(str1)):
      break
    letter = str1[windowEnd]
    if letter in letterTally.keys() or len(letterTally.keys()) < k:
      if letter in letterTally.keys():
        letterTally[letter] += 1
      else:
        letterTally[letter] = 1
      windowEnd += 1
      tempLen += 1
    else:
      maxLen = max(maxLen, tempLen)
      firstLetter = str1[windowStart]
      letterTally[firstLetter] -= 1
      if letterTally[firstLetter] == 0:
        letterTally.pop(firstLetter)
      windowStart += 1
      tempLen -= 1
  return max(maxLen, tempLen)

s = "araaci"
k = 1
print(longest_substring_with_k_distinct(s, k) == 2)

s = "araaci"
k = 2
print(longest_substring_with_k_distinct(s, k) == 4)

s = "cbbebi"
k = 3
print(longest_substring_with_k_distinct(s, k) == 5)

s = "cbbebi"
k = 10
print(longest_substring_with_k_distinct(s, k))# == 6)