题意：
删除链表中值为给定的val的节点。比如：给定链表 1 –> 2 –> 6 –> 3 –> 4 –> 5 和值 val = 6 ，返回 1 –> 2 –> 3 –> 4 –> 5 。

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        while p.next:
            if p.next.val==val:
                p.next=p.next.next
            else:
                p=p.next
        return dummy.next
```

[203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/description/)
