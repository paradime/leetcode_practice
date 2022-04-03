def find_letter_case_string_permutations(str):
  perms = [""]
  for c in str:
    newPerms = []
    for perm in perms:
      if (c.isalpha()):
        newPerms.append(perm+c.upper())
        newPerms.append(perm+c.lower())
      else: 
        newPerms.append(perm+c)
    perms = newPerms
  return perms


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()