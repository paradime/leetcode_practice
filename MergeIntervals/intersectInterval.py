def merge(intervals_a, intervals_b):
  result = []
  i, j = 0, 0
  while (i < len(intervals_a) and j < len(intervals_b)):
    a = intervals_a[i]
    b = intervals_b[j]
    if isOverlap(a, b):
      result.append([
        max(a[0], b[0]),
        min(a[1], b[1])
      ])
    if a[0] <= b[0]:
      i += 1
    else:
      j += 1
  return result

def isOverlap(a, b):
  return ((a[0] <= b[0] and b[0] <= a[1]) 
    or (b[0] <= a[0] and a[0] <= b[1]))

def merge_mine(intervals_a, intervals_b):
  result = []
  for a in intervals_a:
    for b in intervals_b:
      if b[0] <= a[0]:
        start = a[0]
        end = min(b[1], a[1])
        if start <= end:
          result.append([start,end])
      elif a[0] <= b[0]:
        start = b[0]
        end = min(b[1], a[1])
        if start <= end:
          result.append([start,end])
  return result


def main():
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
