def solution(a):
  newArr = []
  for i in range(len(a)):
    newArr.append([])
  for i in range(len(a)-1,-1,-1):
    j = 0
    for val in a[i]:
      newArr[j].append(val)
      j+=1
  return newArr

def solution2(a):
  # reverse over horizontal
  a.reverse()
  #reflect
  for i in range(len(a)):
    for j in range(i,len(a)):
      a[i][j], a[j][i] = a[j][i], a[i][j]
  return a


a = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]
b = [
  [7,4,1],
  [8,5,2],
  [9,6,3],
]
print(solution2(a))