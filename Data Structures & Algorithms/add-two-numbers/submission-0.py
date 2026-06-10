# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = l1  # Keep reference to head
        carry = 0
        prev = None  # Track previous node for potential carry extension
        
        while l1 or l2 or carry:
            # Get values (0 if node doesn't exist)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # If l1 exists, update its value
            if l1:
                l1.val = digit
                prev = l1
                l1 = l1.next
            else:
                # l1 exhausted but l2 or carry remains - extend l1
                prev.next = ListNode(digit)
                prev = prev.next
            
            # Move l2 pointer
            if l2:
                l2 = l2.next
        
        return dummy
        
            

        