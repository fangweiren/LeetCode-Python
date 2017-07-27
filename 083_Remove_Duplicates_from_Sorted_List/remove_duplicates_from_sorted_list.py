# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p = head
        q = head.next
        while q:
            if q.val == p.val:
                q = q.next
	            p.next = q
	        else:
	            p = p.next
	            q = q.next
	    return head
