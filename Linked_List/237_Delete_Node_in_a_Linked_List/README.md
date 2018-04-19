题意  
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.  
写个函数删除一个单链表中的一个节点（非尾节点），该函数的参数是要删除的节点。

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.  
比如一个链表是 1 -> 2 -> 3 -> 4 ，给你一个值为 3 的节点，调用你的函数后链表变成 1 -> 2 -> 4 。

思路  
一般删除一个节点是通过上一个节点来操作，现在只给了当前节点，那么只能将后一节点的值赋给当前节点，将后一节点删掉，则相当于删掉了“当前节点”。

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```
