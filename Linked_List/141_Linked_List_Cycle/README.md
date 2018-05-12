### 题意
Given a linked list, determine if it has a cycle in it.  
给定一个链表，判断链表中是否有环。

Follow up:  
Can you solve it without using extra space?  
你能否不使用额外空间解决此题？

### 思路
沿着链表不断遍历下去，如果遇到空节点就说明该链表不存在环。但如果存在环，这样的遍历就会进入死循环。在环上前进会不断地绕圈子，我们让两个速度不同的指针绕着环前进，那么早晚速度快的那个将追上速度慢的，所以如果速度快的追上了速度慢的，那么该链表就存在环，循环终止。
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```
[LeetCode 141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)
