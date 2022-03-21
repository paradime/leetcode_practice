from __future__ import print_function


class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


# number of merge intervals * number of intervals (O(N*M) == O(n**2))
def merge(intervals):
  tempIntervals = list(intervals)
  merged = []
  i = 0
  merged.append(tempIntervals[i])
  tempIntervals.pop(i)
  while i < len(merged):
    a = merged[i]
    j = 0
    while (j < len(tempIntervals)):
      b = tempIntervals[j]
      if((b.end <= a.end and b.end >= a.start) or 
         (b.start >= a.start and b.start <= a.end) or
         (a.end <= b.end and a.end >= b.end) or
         (a.start >= b.start and a.start <= b.end)):
        merged[i]=(mergeIntervals(a, b))
        a = merged[i]
        tempIntervals.pop(j)
      else:
        merged.append(b)
        j += 1
    i+=1
  return merged

def mergeIntervals(interval1, interval2):
  return Interval(
    min(interval1.start, interval2.start),
    max(interval1.end, interval2.end),
  )

def main():
  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
  print()

main()