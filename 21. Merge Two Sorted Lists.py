"""
1 2 4   1 3 4
a       b

create an empty ListNode
loop until both a and b are len(list) respecitvely
	if bpointer > len(list)
		append apointer into ListNode
		apointer++
		continue
	else if apointer > len(list)
		append apointer into ListNode
		apointer++
		continue
	if value at apointer is greater than value at bpointer,
		append bpointer into ListNode
		bpointer++
		continue
	else
		append apointer into ListNode
		apointer++
		continue
result: 1 --> ( )
               ^result.next
l1: 2 --> 3 --> 4


traverser = result
traverser.next = (node) l2
traverser = traverser.next

result: 1 --> 1 --> ( )

l1 = 3 --> 4

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        #checking if either list is empty
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
    
    
        #creating initial node
        result = ListNode(-1)
        if l1.val > l2.val:
            result.val = l2.val
            l2 = l2.next
        elif l1.val <= l2.val:
            result.val = l1.val
            l1 = l1.next
        
        #creating traverser to go through result node
        traverser = result
        while l1 != None or l2 != None:
            if l1 == None:
                traverser.next = ListNode(l2.val)
                l2 = l2.next
                traverser = traverser.next
            elif l2 == None:
                traverser.next = ListNode(l1.val)
                l1 = l1.next
                traverser = traverser.next
            elif l1.val > l2.val:
                traverser.next = ListNode(l2.val)
                l2 = l2.next
                traverser = traverser.next
            elif l1.val <= l2.val:
                traverser.next = ListNode(l1.val)
                l1 = l1.next
                traverser = traverser.next
        return result
            
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
