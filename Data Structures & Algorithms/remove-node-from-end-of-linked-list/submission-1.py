# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # m = 0
        # curr = head
        
        # while curr:
        #     m += 1
        #     curr = curr.next
        
        # dummy = node = ListNode()

        # curr = head 
        # target = m - n 
        # while curr:
        #     if target == 0:
        #         if curr.next :
        #             node.next = curr.next
        #         else:
        #             node.next = None
        #     else :
        #         node.next = curr
        #         node = node.next
        #     target -= 1
        #     curr = curr.next
        
        # return dummy.next

        dummy = ListNode(0, head)
        left = dummy
        right = head 

        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next


        