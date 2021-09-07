# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slowPointer = head
        if slowPointer == None:
            return False
        fastPointer = head.next
        while slowPointer != fastPointer:
            if fastPointer != None and fastPointer.next != None:
                fastPointer = fastPointer.next.next
                slowPointer = slowPointer.next
            else:
                return False
        if slowPointer == fastPointer:
            return True
