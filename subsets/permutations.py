def find_permutations(nums):
  perms = [[]]
  for num in nums:
    newPerms = []
    for perm in perms:
      tempPerm = list(perm)
      tempPerm.append(num)
      newPerms.append(tempPerm)
      for i in range(len(perm)):
        tempPerm = list(perm)
        tempPerm.insert(i, num)
        newPerms.append(tempPerm)
    perms = newPerms
  return perms


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()