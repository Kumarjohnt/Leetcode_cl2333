# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
        
from heapq import *
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        heap = []
        count = 0
        for i in lists:
            if i:
                count += 1
                heappush(heap, (i.val, count, i))
                
        head, cur = None, None
        while heap:
            _, _, val = heappop(heap)
            if head is None:
                head, cur = val, val
            else:
                cur.next = val
                cur = cur.next
            if val.next:
                count += 1
                heappush(heap, (val.next.val, count, val.next))
                
        return head        
        
        
        