### 题意
Write a program to find the node at which the intersection of two singly linked lists begins.  
编写一个程序，找到两个单链表相交的起始节点。

For example, the following two linked lists:
```
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
```
begin to intersect at node c1.  
在节点 c1 开始相交。

Notes:  
- If the two linked lists have no intersection at all, return null.  
- 如果两个链表没有交点，返回 null.

- The linked lists must retain their original structure after the function returns.  
- 在返回结果后，两个链表仍须保持原有的结构。

- You may assume there are no cycles anywhere in the entire linked structure.  
- 可假定整个链表结构中没有循环。

- Your code should preferably run in O(n) time and use only O(1) memory.  
- 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

### 思路
本题我们关心的是让两个链表的指针同时到达交叉点。定义两个指针，让它们将两个链表都遍历一遍，那么它们的总长度是一样的，倘若两个链表相交，那么这两个指针一定会在某个地方相等。
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        pa = headA
        pb = headB
        while pa and pb and pa != pb:
            pa = pa.next
            pb = pb.next
            if pa == pb:
                return pa
            if not pa:
                pa = headB
            if not pb:
                pb = headA
        return pa


#---------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pa = headA
        pb = headB
        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa
```
[LeetCode 160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/description/)
