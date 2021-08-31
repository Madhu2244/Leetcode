# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_length = 1
        traveler = head
        while traveler.next is not None:
            total_length += 1
            traveler = traveler.next
        if total_length == 1:
            return None
        traveler = head
        if n == total_length:
            return traveler.next
        if n != 1:
            cnt = 1
            while cnt < total_length - n:
                traveler = traveler.next
                cnt += 1
            print(traveler.val)
            prenode = traveler
            print(prenode.val)    
            traveler = traveler.next
            traveler = traveler.next
            postnode = traveler
            print(postnode.val)
            prenode.next = postnode
            return head
        else:
            cnt = 1
            while cnt < total_length - 1:
                traveler = traveler.next
                cnt +=1
            traveler.next = None
            return head
            
