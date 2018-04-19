题意  
Reverse a singly linked list.  
反转一个单链表。

click to show more hints.

Hint:  
A linked list can be reversed either iteratively or recursively. Could you implement both?  
链表可以迭代或递归地反转。 你能否实现两者？

思路  
直接在原链表操作，通过迭代将节点重组，前面的节点转移到重组链表的后面。实际上就是头结点倒插操作。

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head
```
[LeetCode 206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)  
[206. Reverse Linked List [easy] (Python)](https://blog.csdn.net/coder_orz/article/details/51306170)
