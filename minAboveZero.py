def solution(A):
  A.sort()
  min = 1
  for val in A:
    if val <= 0:
      continue
    if val == min:
      min += 1
  return min

inp = [1,2,3]
print(solution(inp) == 4)
inp = [-1,-3]
print(solution(inp) == 1)