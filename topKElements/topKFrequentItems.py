from heapq import heappop, heappush


def find_k_frequent_numbers(nums, k):
  minHeap = []
  letterCount = convertToLetterCount(nums)
  # (freq, num)
  letterCountTuples = list(map(lambda kv: (kv[1], kv[0]), letterCount.items()))
  for i in range(k):
    record = letterCountTuples[i]
    heappush(minHeap, record)
  for i in range(k, len(letterCountTuples)):
    record = letterCountTuples[i]
    if minHeap[0][0] < record[0]:
      heappop(minHeap)
      heappush(minHeap, record)
  return list(map(lambda x: x[1], minHeap))

def convertToLetterCount(nums):
  letterCount = {}
  for num in nums:
    if num in letterCount.keys():
      letterCount[num]+=1
    else:
      letterCount[num] = 1
  return letterCount

def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()


