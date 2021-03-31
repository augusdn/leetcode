# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(val=0, next=None)
        last = result
        flag = 0
        
        while l1 or l2 or flag:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            flag, remainder = divmod(val1+val2+flag, 10)
            
            last.next = ListNode(remainder)
            last = last.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return result.next
