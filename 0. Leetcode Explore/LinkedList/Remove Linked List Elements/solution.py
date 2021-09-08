# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prevNode = None
        travelerNode = head
        #first we need to get rid of all the elements in the beginning equal to val
        while travelerNode and travelerNode.val == val:
            if travelerNode.next:
                head = travelerNode.next
                travelerNode = head
            else:
                head = None
                return head
        #the first value is not equal to val here
        prevNode = head
        while travelerNode and travelerNode.next:
            if travelerNode.val == val:
                prevNode.next = travelerNode.next
                travelerNode = travelerNode.next
            else:
                prevNode = travelerNode
                travelerNode = travelerNode.next
        if travelerNode and travelerNode.val == val:
            prevNode.next = None
        return head
            
