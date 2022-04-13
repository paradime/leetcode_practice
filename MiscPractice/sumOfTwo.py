def solution(a, b, v):
  bSet = set(b)
  for val in a:
    if v-val in bSet:
      return True
  return False

a = [1,2,3]
b = [10,20,30,40]
v = 42
print(solution(a,b,v) == True)