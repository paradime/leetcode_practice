def find_happy_number_mine(num):
  curNum = num
  seen = set()
  while(True):
    dSquare = digitSquare(curNum)
    if dSquare == 1:
      return True
    if dSquare in seen:
      return False
    seen.add(dSquare)
    curNum = dSquare

def find_happy_number(num):
  slow, fast = num, digitSquare(num)
  while (fast!=slow):
    slow = digitSquare(slow)
    fast = digitSquare(digitSquare(fast))
  return fast == 1

def digitSquare(num):
  numStr = str(num)
  digitSquare = 0
  for c in numStr:
    digitSquare += int(c)**2
  return digitSquare

def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()
