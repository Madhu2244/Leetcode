# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        listALength = 0
        listBLength = 0
        aTraveler = headA
        while aTraveler:
            listALength += 1
            aTraveler = aTraveler.next
            
        bTraveler = headB
        while bTraveler:
            listBLength += 1
            bTraveler = bTraveler.next
        skipDistance = abs(listALength - listBLength)
        aTraveler = headA
        bTraveler = headB
        if listALength > listBLength:
            while skipDistance > 0:
                skipDistance -= 1
                aTraveler = aTraveler.next
        else:
            while skipDistance > 0:
                skipDistance -= 1
                bTraveler = bTraveler.next
        while aTraveler and bTraveler:
            if aTraveler == bTraveler:
                return aTraveler
            aTraveler = aTraveler.next
            bTraveler = bTraveler.next
        return None
