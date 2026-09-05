# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid

        if head.next == None:
            return 
        curr = head
        slow, fast = curr, curr.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        reverse, curr = None, slow.next
        slow.next = None

        while curr:
            temp = curr.next

            curr.next = reverse
            reverse = curr

            curr = temp
        
        curr = head
        while reverse:

            temp1, temp2 = curr.next, reverse.next
            print(curr.val)
            print(reverse.val)
            curr.next = reverse
            reverse.next = temp1

            curr, reverse = temp1, temp2



