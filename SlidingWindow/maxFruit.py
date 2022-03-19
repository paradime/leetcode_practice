def fruits_into_baskets(fruits):
  maxFruit = 0
  baskets = {}
  windowStart, windowEnd = 0,0
  while windowStart < len(fruits) and windowEnd < len(fruits):
    lastFruit = fruits[windowEnd]
    firstFruit = fruits[windowStart]
    if lastFruit in baskets.keys() or len(baskets.keys()) < 2:
      if lastFruit not in baskets.keys():
        baskets[lastFruit] = 1
      else:
        baskets[lastFruit] += 1
      windowEnd += 1
    else:
      maxFruit = max(sum(baskets.values()), maxFruit)
      if baskets[firstFruit] == 1:
        baskets.pop(firstFruit)
      else:
        baskets[firstFruit] -= 1
      windowStart += 1
  return max(maxFruit, sum(baskets.values()))

fruits = ['A', 'B', 'C', 'A', 'C']
print(fruits_into_baskets(fruits) == 3)

fruits = ['A', 'B', 'C', 'B', 'B', 'C']
print(fruits_into_baskets(fruits) == 5)