# Add two numbers represented by linked lists 

# Given two numbers represented by two lists, write a function that returns the sum list. The sum list is a list representation of the addition of two input numbers.

# Input: 
# List1: 5->6->3 // represents number 365 
# List2: 8->4->2 // represents number 248 
# Output: 
# Resultant list: 3->1->6 // represents number 613 
# Explanation: 365 + 248 = 613
# Input: 
# List1: 7->5->9->4->6 // represents number 64957 
# List2: 8->4 // represents number 48 
# Output: 
# Resultant list: 5->0->0->5->6 // represents number 65005 
# Explanation: 64957 + 48 = 65005.. 


class Node:
    def __init__(self, next, val):
        self.next =next
        self.val = val

def printLL(head):
    curNode = head
    while(curNode!= None):
        print(curNode.val)
        curNode = curNode.next

def addLL(head1, head2):
    curNode1 = head1
    curNode2 = head2
    # newVal = 0
    # if curNode1 != None:
    #     newVal += curNode1.val
    # if curNode2 != None:
    #     newVal += curNode2.val
    # if curNode1 != None:
    #     curNode1 = curNode1.next
    # if curNode2 != None:
    #     curNode2 = curNode2.next
    # if newVal >= 10:
    #     carryover =1
    #     newVal -= 10
    # else:
    newCur = None
    # prevCur = Node(None, 0)
    newHead = currNode
    carryover = 0
    while curNode1 != None or curNode2 != None:
        newVal = carryover
        if curNode1 != None:
            newVal += curNode1.val
        if curNode2 != None:
            newVal += curNode2.val

        carryover = newVal/10
        newVal = newVal % 10
            
        newCur = Node(None, 0)
        if(currNode == None):
            currNode = Node(None, newVal)
            newHead = currNode

        currNode.val = newVal
        if(preNode != None):
            preNode.next = currNode
        preNode = currNode

        if curNode1 != None:
            curNode1 = curNode1.next
        if curNode2 != None:
            curNode2 = curNode2.next
    return newHead


head = Node(None, 5)
head.next = Node(None, 6)
head.next.next = Node(None, 3)
head2 = Node(None, 8)
head2.next = Node(None, 4)
head2.next.next = Node(None, 2)
printLL(addLL(head, head2))

