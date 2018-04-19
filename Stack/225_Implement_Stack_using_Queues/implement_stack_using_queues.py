class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = collections.deque([])
									        
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for i in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())

		self.stack.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.stack) == 0
