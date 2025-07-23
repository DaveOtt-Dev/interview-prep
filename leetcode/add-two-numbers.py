# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        curr = l3

        carry = 0
        while l1 is not None or l2 is not None:
            val = carry
            if l1 is not None:
                val += l1.val
            if l2 is not None:
                val += l2.val

            curr.next = ListNode()

            if val < 10:
                carry = 0
                curr.next.val = val
            else:
                carry = 1
                curr.next.val = val - 10
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            curr = curr.next
        
        if carry != 0:
            curr.next = ListNode(carry)

        return l3.next
