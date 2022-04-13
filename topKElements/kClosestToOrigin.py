from heapq import heappop, heappush


class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

def find_closest_points(points, k):
  maxHeap = []
  for i in range(k):
    point = points[i]
    distance = point.x**2 + point.y**2
    heappush(maxHeap, (-distance, point))
  for i in range(k, len(points)):
    point = points[i]
    distance = point.x**2 + point.y**2
    if maxHeap[0][0] < -distance:
      heappop(maxHeap)
      heappush(maxHeap, (-distance, point))
  return map(lambda x: x[1], maxHeap)


def main():
  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()

main()