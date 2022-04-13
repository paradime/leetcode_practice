from heapq import heapify, heappop, heappush


def minimum_cost_to_connect_ropes(ropes):
  cost = 0
  heapify(ropes)
  while(len(ropes) > 1):
    rope1 = heappop(ropes)
    rope2 = heappop(ropes)
    newRope = rope1+rope2
    cost += newRope
    heappush(ropes, newRope)
  return cost


def main():

  print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()