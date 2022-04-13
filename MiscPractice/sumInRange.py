from dataclasses import dataclass
from functools import cache

def solution(nums, queries):
    qSum = []
    cached = {}
    for q in queries:
      maxQ = min(q[1]+1, len(nums))
      if (q[0], maxQ) in cached:
        qSum.append(cached[(q[0], maxQ)])
      else:
        qSum.append(sumVals(nums,q[0], maxQ))
        cached[(0,2)] = sumVals
    return sum(qSum) % (10**9 +7)

def sumVals(nums, i, j):
  return sum(nums[i:j])

def solution2(nums,queries):
  dp = []
  for i in range(len(nums)):
    dp.append([])
    for j in range(len(nums)):
      if i == j:
        dp[-1].append(nums[i])
      else:
        dp[-1].append(False)
  qSum = []
  for q in queries:
    maxQ = min(q[1], len(nums)-1)
    qSum.append(getValRecurse(dp, q[0], maxQ, nums))
  return sum(qSum) % (10**9 +7)

def getValRecurse(dp, i, j, nums):
  if dp[i][j]!= False:
    return dp[i][j]
  else:
    dp[i][j] = getValRecurse(dp, i, j-1, nums)+nums[j]
    return dp[i][j]

def solution3(nums, queries):
  s = 0
  prefixSums = [0]
  for num in nums:
    s += num
    prefixSums.append(s)
  qSums = []
  for q in queries:
    qSums.append(prefixSums[q[1]+1]-prefixSums[q[0]])
  return sum(qSums)


nums = [3, 0, -2, 6, -3, 2]
queries = [[0,2], 
 [2,5], 
 [0,5]]
print(solution3(nums, queries))# == 10)