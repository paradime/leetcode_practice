"""
Suppose we have two lists of signed integers in ascending order, a and b. Write a function that takes these two ordered lists as well as an integer argument limit that returns a merged list with limit elements in ascending order.

a = [1, 3, 5] # O(n)
b = [2, 6, 8, 9] # O(n) 
limit = 3 O(L) # O(1)

=> [1, 2, 3] # O(1)

list, list, int -> list

a = [1]
b = [2]
limit = 1

[1]

a = [2]
b = [1]
list = 1

=> [1]
"""

a = [1, 3, 5]
b = [2, 6, 8, 9]
limit = 3

a = []
b = []
limit = 1

# => [1]

def smallest_items(list1, list2, limit):
    result = []*limit
    for i in range(limit):
        if (len(list1) == 0 and len(list2) == 0):
            return result
        elif(len(list1) == 0):
            result.append(list2[0])
            list2.pop(0)
        elif(len(list2) == 0):
            result.append(list1[0])
            list1.pop(0)
        elif(list1[0] < list2[0]):
            result.append(list1[0])
            list1.pop(0)
        else:
            result.append(list2[0])
            list2.pop(0)
    return result

[1] - 1 - 1
[2] -

[3] - 3 - 
[4] -

print(smallest_items(a, b, limit) == [])

ind_list1

ind_list2
[0,1,2]

[0,1,2]
[0,1,2,3]
