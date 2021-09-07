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
        if slowPointer.next == None:
            return False
        if slowPointer.next.next == None:
            return False
        fastPointer = head.next.next
        while slowPointer != fastPointer:
            if fastPointer.next != None:
                fastPointer = fastPointer.next
                if fastPointer.next != None:
                    fastPointer = fastPointer.next
                    slowPointer = slowPointer.next
                else:
                    return False
            else:
                return False
        if slowPointer == fastPointer:
            return True
