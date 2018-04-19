题意  
Given a singly linked list, determine if it is a palindrome.  
给定一个单链表，判断是否是“ 回文链表”。

Follow up:  
进一步

Could you do it in O(n) time and O(1) space?  
你能在时间复杂度 O(n) 和空间复杂度 O(1) 下完成该问题吗？

思路  
提取链表中的 val, 加入到 list 中，然后进行判断。

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = []
        while head:
            vals += head.val,
            head = head.next
        return vals == vals[::-1]
```

[234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/description/)
