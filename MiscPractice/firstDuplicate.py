def solution(a):
  seen = set()
  for num in a:
    if num in seen:
      return num
    seen.add(num)
  return -1


a = [2,1,3,5,3,2]
out = 3
print(solution(a) == 3)
a = [2,2] 
out = 2
print(solution(a) == out)
a = [2,4,3,5,1] 
out = -1
print(solution(a) == out)