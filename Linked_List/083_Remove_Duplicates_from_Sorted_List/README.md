### 题意
Given a sorted linked list, delete all duplicates such that each element appear only once.  
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

Example 1:
```
Input: 1->1->2
Output: 1->2
```
Example 2:
```
Input: 1->1->2->3->3
Output: 1->2->3
```
### 思路
遍历所有节点，对于每个节点，从后一个节点开始一个个检查是否与当前节点值相同，直到找到一个后面的节点其值与当前节点不同，删除中间的所有与当前节点值相同的节点。
```python
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
```
[LeetCode 83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/discuss/129967/Accepted-easy-understanding-python-solution)
