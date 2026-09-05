# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode()
        pq = []

        for item in lists:
            heapq.heappush(pq, (item.val, id(item), item))
        
        while pq:
            _, _, item = heapq.heappop(pq)
            node.next = item
            node = node.next

            item = item.next
            if item:
                heapq.heappush(pq, (item.val, id(item), item))

        return dummy.next