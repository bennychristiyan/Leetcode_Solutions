#Problem
"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their 
nodes contains a single digit. Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading 
zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807."""

# Normally, we have to do addition from right to left. But, since it is in reverse order, it is much easier for us to add(from left to right)

# Time complexity = O(max(n1, n2)). Runtime = 45ms (Beats 95.10%)
class ListNode:
    # Creates a new node. If no value is given, default value 0 is given
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        
        # Create a dummy node with value 0 and point cur to dummy
        dummy = ListNode()
        cur = dummy

        carry = 0
        
        # The loop will run until there is a node in l1 or l2 or there is a carry value
        while l1 or l2 or carry:

            # v1 and v2 stores the node value if present; else stores value 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Add v1, v2 and carry and store it in a variable val
            val = v1 + v2 + carry
            # The carry is calculated by floor division of val and 10. If val is less than 10, it stores 0; else the tenth place digit is stored
            carry = val // 10
            # The val is updated by doing modulo of val and 10. The unit digit val is stored in val
            val = val % 10

            # Initially cur points to the node 0    
            # The val is turned into a node and appended with the cur 
            cur.next = ListNode(val)
            
            # Updates cur pointer to the newly appended node
            cur = cur.next
            # Updates the l1 and l2 to be the next node for next iteration. If node is not present, None is returned
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # After the loop is finished, the result is next to the dummy node. Therefore, we return the LinkedList after the dummy node
        return dummy.next


        