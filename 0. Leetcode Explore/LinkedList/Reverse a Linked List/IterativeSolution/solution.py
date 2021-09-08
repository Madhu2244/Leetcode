# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        if not head:
            return head
        if not head.next:
            return head
        nextNode = head.next
        currNode = head
        while currNode.next:
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
            nextNode = nextNode.next
        currNode.next = prevNode
        return currNode
