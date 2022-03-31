def solution(prices, notes, x):
  denoms = findDiscountDenoms(notes)
  deltas = 0
  for i in range(len(prices)):
    delta = prices[i] - (prices[i]*100)/(100+denoms[i])
    print(delta)
    deltas += delta
  return deltas <= x

def findDiscountDenoms(notes):
  denoms = []
  for note in notes:
    words = note.split(' ')
    if words[0] == 'Same':
      denoms.append(0)
      continue
    val = float(words[0].split('%')[0])
    val *= 1 if words[1] == "higher" else -1
    denoms.append(val)
  return denoms


prices = [110, 95, 70]
notes = ["10.0% higher than in-store", 
         "5.0% lower than in-store", 
         "Same as in-store"]
x = 5
print(solution(prices,notes,x))#==True)

prices = [48, 165]
notes = ["20.00% lower than in-store", 
         "10.00% higher than in-store"]
x = 2
print(solution(prices,notes,x))#==True)