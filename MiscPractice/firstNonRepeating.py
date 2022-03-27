def solution(s):
  letterCount = {}
  seen = []
  for char in s:
    if char in letterCount.keys():
      letterCount[char] += 1
    else:
      letterCount[char] = 1
      seen.append(char)
  for char in seen:
    if letterCount[char] == 1:
      return char
  return "_"


s = "abacabad"
out = 'c'
print(solution(s) == out)

s = "abacabaabacaba"
out = '_'
print(solution(s) == out)