#User function Template for python3
class TwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Function to push an integer into stack 1
    def push1(self, x):
        self.stack1.append(x)

    # Function to push an integer into stack 2
    def push2(self, x):
        self.stack2.append(x)

    def isEmpty1(self):
        return len(self.stack1) == 0
        
    def isEmpty2(self):
        return len(self.stack2) == 0

    # Function to remove an element from top of stack 1
    def pop1(self):
        if not self.isEmpty1():
            return self.stack1.pop()
        return -1
