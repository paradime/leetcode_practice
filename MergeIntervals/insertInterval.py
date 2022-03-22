def insert(intervals, new_interval):
  intervals = insertInterval(new_interval, intervals)
  merged = mergeSortedIntervals(intervals)
  return merged

def mergeSortedIntervals(intervals):
  merged = []
  i = 0
  merged.append(intervals[i])
  intervals.pop(i)
  a = merged[i]
  while i < len(merged):
    a = merged[i]
    j = 0
    while j < len(intervals):
      b = intervals[j]
      if a[0] <= b[0] and b[0] <= a[1]:
        merged[i] = mergeIntervals(a,b)
        intervals.pop(j)
      else:
        merged.append(b)
        break
    i += 1
  return merged

def mergeIntervals(a, b):
  return [min(a[0], b[0]), max(a[1], b[1])]
# insert into list:
#   for interval in intervals:
#     if intsertingInterval.start < interval.start:
#       insert into this location
def insertInterval(interval, intervals):
  i = 0
  while i < len(intervals):
    if (interval[0] < intervals[i][0]):
      intervals.insert(i, interval)
      break
    i += 1
  return intervals

def main():
  print(mergeIntervals([1,2], [2,3]))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
