# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head 
        slow, fast = curr, curr.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        second = slow.next
        slow.next = None

        # Rever second

        prev, curr = None, second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first, second = head, prev

        while second:
            nxt1, nxt2 = first.next, second.next

            first.next = second
            second.next = nxt1

            first, second = nxt1, nxt2
        
        

