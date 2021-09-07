# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 3 2 0 -4 (-4 loops back to 2)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return None
        slowPointer = head # 3
        fastPointer = head.next # 2
        while fastPointer != None and fastPointer.next != None: # 2.next != None, #-4.next != None, #0.next != None
            if slowPointer == fastPointer: #0 = 0
                slowPointer = head # 3
                fastPointer = fastPointer.next
                while slowPointer != fastPointer:
                    slowPointer = slowPointer.next # 2
                    fastPointer = fastPointer.next
                return slowPointer
            slowPointer = slowPointer.next # 2, # 0 # -4 
            fastPointer = fastPointer.next.next # -4, # 0
        return None
