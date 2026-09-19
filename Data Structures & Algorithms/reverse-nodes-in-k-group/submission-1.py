# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:


        dummy = ListNode(0, head)
        prevGroup = dummy

        while True:

            kth = self.getKthNode(prevGroup, k)
            if not kth:
                break
            nextGroup = kth.next


            prev, curr = kth.next, prevGroup.next

            while curr!=nextGroup:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            tmp = prevGroup.next
            prevGroup.next = kth
            prevGroup = tmp
        return dummy.next     


    def getKthNode(self, curr, k):
        while curr and k > 0:
            k -= 1
            curr = curr.next
        
        return curr 
        