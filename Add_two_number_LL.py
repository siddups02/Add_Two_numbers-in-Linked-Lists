# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
        # @return a ListNode
        def addTwoNumbers(self, l1, l2):
            carry = 0  # This will hold the carry produced during the addition
            root = n = ListNode(0) # creating 2 empty List for solution to be held on
            while l1 or l2 or carry: # Checking if L1, L2 Lists and carry is not zero
                val1 = val2 = 0 # Creating two variables to hold each element from the list everytime
                if l1:
                    val1 = l1.val  # going through each value from the list L1 and putting it to val1
                    l1 = l1.next
                if l2:
                    val2 = l2.val  # going through each value from the list L2 and putting it to val2
                    l2 = l2.next

                # sum = (val1+val2+carry)%10  # Line 21 and 22 have the same calculation but 20ms slower
                # carry = int((val1+val2+carry)/10)
                carry, sum = divmod(val1+val2+carry, 10) # Forming Sum and carry using faster Solution
                n.next = ListNode(sum)  # Adding the Sum to new List 'n' 
                n = n.next

            return root.next  # O(n) solution
